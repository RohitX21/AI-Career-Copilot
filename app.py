import streamlit as st

from resume_parser import extract_text
from resume_analyzer import analyze_resume
from skill_gap import skill_gap_analysis
from roadmap_generator import generate_roadmap
from interview_generator import generate_questions

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖"
)

st.title("🤖 AI Career Copilot")

st.write(
    "Upload your resume and get AI-powered career guidance."
)

# Resume Upload
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    # Extract Resume Text
    resume_text = extract_text(uploaded_file)

    st.success("Resume Uploaded Successfully!")

    # Optional Preview
    with st.expander("View Extracted Resume Text"):
        st.write(resume_text)

    # Target Role
    role = st.text_input(
        "Enter Target Role",
        placeholder="Example: Software Engineer"
    )

    st.divider()

    # Resume Analysis
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(resume_text)

        st.subheader("📄 Resume Analysis")
        st.write(result)

    st.divider()

    # Skill Gap Analysis
    if role:

        if st.button("Skill Gap Analysis"):

            with st.spinner("Finding Skill Gaps..."):

                result = skill_gap_analysis(
                    resume_text,
                    role
                )

            st.subheader("🎯 Skill Gap Analysis")
            st.write(result)

    st.divider()

    # Roadmap Generation
    if role:

        if st.button("Generate Roadmap"):

            with st.spinner("Creating Roadmap..."):

                roadmap = generate_roadmap(
                    resume_text,
                    role
                )

            st.subheader("🗺️ Learning Roadmap")
            st.write(roadmap)

    st.divider()

    # Interview Questions
    if st.button("Generate Interview Questions"):

        with st.spinner("Generating Questions..."):

            questions = generate_questions(
                resume_text
            )

        st.subheader("🎤 Mock Interview Questions")
        st.write(questions)

else:

    st.info("Please upload a resume to begin.")
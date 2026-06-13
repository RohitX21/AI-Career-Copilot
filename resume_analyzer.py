import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_resume(text):

    prompt = f"""
    Analyze this resume.

    Give:

    1. Strengths
    2. Weaknesses
    3. ATS Score
    4. Suggestions

    Resume:

    {text}
    """

    response = model.generate_content(
        prompt
    )

    return response.text
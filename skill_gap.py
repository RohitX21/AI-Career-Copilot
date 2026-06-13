import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def skill_gap_analysis(
        resume_text,
        role):

    prompt = f"""
    Resume:

    {resume_text}

    Target Role:

    {role}

    Tell me:

    1. Current Skills

    2. Missing Skills

    3. Learning Suggestions
    """

    response = model.generate_content(
        prompt
    )

    return response.text
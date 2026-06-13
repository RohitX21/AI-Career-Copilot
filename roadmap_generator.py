import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_roadmap(
        resume_text,
        role):

    prompt = f"""
    Create a 3 month roadmap.

    Current Resume:

    {resume_text}

    Target Role:

    {role}

    Give week wise plan.
    """

    response = model.generate_content(
        prompt
    )

    return response.text
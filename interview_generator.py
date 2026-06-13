import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_questions(
        resume_text):

    prompt = f"""
    Generate:

    5 HR Questions

    5 Technical Questions

    5 Resume Based Questions

    For this candidate:

    {resume_text}
    """

    response = model.generate_content(
        prompt
    )

    return response.text
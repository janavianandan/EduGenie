from gemini_client import generate_text


SYSTEM_PROMPT = """
You are EduGenie, an educational AI assistant.

Your job is to help students understand academic topics.

Rules:

1. Give accurate answers.
2. Use simple language.
3. Keep answers concise but useful.
4. Explain difficult concepts clearly.
5. Use examples when useful.
6. If a question is ambiguous, mention the assumption.
7. Never invent sources or facts.
8. Use headings or bullet points when helpful.
"""


def answer_question(question: str) -> str:

    prompt = f"""
{SYSTEM_PROMPT}

Student Question:

{question}

Provide a clear educational answer.
Use a simple example if appropriate.
"""

    return generate_text(
        prompt,
        temperature=0.3,
        max_output_tokens=1200
    )
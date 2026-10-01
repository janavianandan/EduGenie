from gemini_client import generate_text


def summarize_text(text: str) -> str:

    prompt = f"""
You are EduGenie, a study assistant.

Summarize the following educational passage.

Requirements:

- Keep the important information.
- Remove unnecessary repetition.
- Use simple language.
- Make it useful for exam revision.

Format:

Short Summary

Key Points

Important Terms

Educational Passage:

{text}
"""

    return generate_text(

        prompt,

        temperature=0.2,

        max_output_tokens=1800
    )
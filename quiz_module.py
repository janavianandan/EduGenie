import json
import re

from gemini_client import generate_json


QUIZ_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": {"type": "string"},
            "options": {
                "type": "array",
                "items": {"type": "string"}
            },
            "correct_answer": {"type": "string"}
        },
        "required": [
            "question",
            "options",
            "correct_answer"
        ]
    }
}


def clean_json_block(text: str) -> str:
    text = text.strip()

    text = re.sub(
        r"^```(?:json)?\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r"\s*```$", "", text)

    return text.strip()


def generate_quiz(passage: str, count: int = 3):

    count = max(1, min(count, 10))

    prompt = f"""
Create exactly {count} multiple-choice questions
from the following topic.

Topic:
{passage}

Rules:
- Each question must have exactly 4 options.
- Only one option must be correct.
- correct_answer must exactly match one option.
- Do NOT provide explanations.
- Return ONLY valid JSON.
- Do not use Markdown.

Format:

[
  {{
    "question": "Question here",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Option A"
  }}
]
"""

    raw = generate_json(
        prompt,
        QUIZ_SCHEMA,
        max_output_tokens=3000
    )

    cleaned = clean_json_block(raw)

    try:
        quiz = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Quiz JSON parsing failed: {exc}"
        ) from exc

    if not isinstance(quiz, list):
        raise RuntimeError(
            "Quiz response must be a JSON array."
        )

    validated = []

    for index, item in enumerate(quiz, start=1):

        question = str(
            item.get("question", "")
        ).strip()

        options = item.get("options", [])

        correct_answer = str(
            item.get("correct_answer", "")
        ).strip()

        if not question:
            raise RuntimeError(
                f"Quiz item {index} has no question."
            )

        if not isinstance(options, list):
            raise RuntimeError(
                f"Quiz item {index} options are invalid."
            )

        if len(options) != 4:
            raise RuntimeError(
                f"Quiz item {index} must have exactly 4 options."
            )

        options = [
            str(option).strip()
            for option in options
        ]

        if correct_answer not in options:
            raise RuntimeError(
                f"Quiz item {index} has an invalid correct answer."
            )

        validated.append({
            "question": question,
            "options": options,
            "correct_answer": correct_answer
        })

    return validated
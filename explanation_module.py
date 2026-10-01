from functools import lru_cache

from config import USE_LOCAL_EXPLAINER, LOCAL_EXPLAINER_MODEL
from gemini_client import generate_text


@lru_cache(maxsize=1)
def get_local_explainer():
    if not USE_LOCAL_EXPLAINER:
        return None

    try:
        from transformers import pipeline
    except ImportError as exc:
        raise RuntimeError(
            "Local explainer dependencies are not installed. "
            "Set USE_LOCAL_EXPLAINER=false or install "
            "transformers, torch, and sentencepiece."
        ) from exc

    return pipeline(
        "text2text-generation",
        model=LOCAL_EXPLAINER_MODEL
    )


def explain_concept(topic: str) -> str:

    if USE_LOCAL_EXPLAINER:
        explainer = get_local_explainer()

        prompt = (
            "Explain the following concept for a beginner engineering "
            "student using simple words and one example:\n\n"
            f"{topic}"
        )

        result = explainer(
            prompt,
            max_new_tokens=220,
            do_sample=False
        )

        return result[0]["generated_text"].strip()

    prompt = f"""
You are EduGenie, a patient teacher.

Explain this concept to a beginner engineering student:

{topic}

Use:
1. Simple definition
2. How it works
3. One easy example
4. Key points to remember

Avoid unnecessary jargon.
"""

    return generate_text(
        prompt,
        temperature=0.3,
        max_output_tokens=1200
    )
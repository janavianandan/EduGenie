from gemini_client import generate_text


def get_learning_recommendations(
    topic: str
) -> str:

    prompt = f"""
You are EduGenie, a personalized learning advisor.

Create a complete learning path for:

{topic}

Assume the student is a beginner.

Organize the learning path into:

1. Beginner Level
2. Intermediate Level
3. Advanced Level

For each level include:

- Topics to learn
- Suggested duration
- Practice activities
- Small projects
- Recommended resource types

At the end provide:

- Weekly study schedule
- Practice checklist
- Revision strategy

Do not invent specific URLs.
Keep the plan practical and student-friendly.
"""

    return generate_text(

        prompt,

        temperature=0.4,

        max_output_tokens=2500
    )
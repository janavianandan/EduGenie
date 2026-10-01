from functools import lru_cache
import time

from config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiConfigurationError(RuntimeError):
    pass


@lru_cache(maxsize=1)
def get_client():

    if not GEMINI_API_KEY:
        raise GeminiConfigurationError(
            "GEMINI_API_KEY is not configured. "
            "Add it to the .env file."
        )

    try:
        from google import genai

    except ImportError as exc:

        raise GeminiConfigurationError(
            "Google GenAI SDK is not installed. "
            "Run: pip install -r requirements.txt"
        ) from exc

    return genai.Client(
        api_key=GEMINI_API_KEY
    )


def generate_text(
    prompt: str,
    temperature: float = 0.4,
    max_output_tokens: int = 2048
) -> str:

    client = get_client()

    from google.genai import types

    last_error = None

    for attempt in range(4):

        try:

            response = client.models.generate_content(

                model=GEMINI_MODEL,

                contents=prompt,

                config=types.GenerateContentConfig(
                    temperature=temperature,
                    max_output_tokens=max_output_tokens
                )
            )

            text = getattr(
                response,
                "text",
                None
            )

            if not text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return text.strip()

        except Exception as exc:

            last_error = exc

            error_text = str(exc)

            if "503" not in error_text:
                raise

            if attempt < 3:

                wait_time = 2 ** attempt

                time.sleep(wait_time)

            else:

                raise RuntimeError(
                    "Gemini service is temporarily busy. "
                    "Please try again in a few minutes."
                ) from last_error


def generate_json(
    prompt: str,
    schema,
    max_output_tokens: int = 3000
):

    client = get_client()

    from google.genai import types

    last_error = None

    for attempt in range(4):

        try:

            response = client.models.generate_content(

                model=GEMINI_MODEL,

                contents=prompt,

                config=types.GenerateContentConfig(

                    temperature=0.3,

                    max_output_tokens=max_output_tokens,

                    response_mime_type="application/json",

                    response_schema=schema
                )
            )

            text = getattr(
                response,
                "text",
                None
            )

            if not text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return text.strip()

        except Exception as exc:

            last_error = exc

            error_text = str(exc)

            if "503" not in error_text:
                raise

            if attempt < 3:

                wait_time = 2 ** attempt

                time.sleep(wait_time)

            else:

                raise RuntimeError(
                    "Gemini service is temporarily busy. "
                    "Please try again in a few minutes."
                ) from last_error
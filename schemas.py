from typing import Any

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------
# NORMAL TEXT REQUEST
# ---------------------------------------------------------

class TextRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=2,
        max_length=12000
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:

        value = value.strip()

        if not value:
            raise ValueError(
                "Input cannot be empty."
            )

        return value


# ---------------------------------------------------------
# QUIZ REQUEST
# ---------------------------------------------------------

class QuizRequest(TextRequest):

    count: int = Field(
        default=3,
        ge=1,
        le=10
    )


# ---------------------------------------------------------
# COMMON API RESPONSE
# ---------------------------------------------------------

class APIResponse(BaseModel):

    success: bool

    result: Any
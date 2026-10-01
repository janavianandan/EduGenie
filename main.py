from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import TextRequest, QuizRequest, APIResponse
from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    description="AI-powered educational assistant for students",
    version="1.0.0",
)


# ---------------------------------------------------------
# Static Files and Templates
# ---------------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


# ---------------------------------------------------------
# Home Page
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "EduGenie"
        }
    )


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "EduGenie API is running"
    }


# ---------------------------------------------------------
# Question & Answer
# ---------------------------------------------------------

@app.post("/qa", response_model=APIResponse)
async def qa(request: TextRequest):

    try:
        result = answer_question(request.text)

        return APIResponse(
            success=True,
            result=result
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Q&A failed: {str(exc)}"
        )


# ---------------------------------------------------------
# Explain Concept
# ---------------------------------------------------------

@app.post("/explain", response_model=APIResponse)
async def explain(request: TextRequest):

    try:
        result = explain_concept(request.text)

        return APIResponse(
            success=True,
            result=result
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Explanation failed: {str(exc)}"
        )


# ---------------------------------------------------------
# Generate Quiz
# ---------------------------------------------------------

@app.post("/quiz", response_model=APIResponse)
async def quiz(request: QuizRequest):

    try:
        result = generate_quiz(
            request.text,
            request.count
        )

        return APIResponse(
            success=True,
            result=result
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Quiz generation failed: {str(exc)}"
        )


# ---------------------------------------------------------
# Summarize Text
# ---------------------------------------------------------

@app.post("/summarize", response_model=APIResponse)
async def summarize(request: TextRequest):

    try:
        result = summarize_text(request.text)

        return APIResponse(
            success=True,
            result=result
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Summarization failed: {str(exc)}"
        )


# ---------------------------------------------------------
# Learning Path Recommendations
# ---------------------------------------------------------

@app.post(
    "/learn/recommendations",
    response_model=APIResponse
)
async def learning_recommendations(request: TextRequest):

    try:
        result = get_learning_recommendations(
            request.text
        )

        return APIResponse(
            success=True,
            result=result
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Learning recommendation failed: {str(exc)}"
        )
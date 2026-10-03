# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant designed to simplify learning through Generative AI.

It helps students with:

* Question Answering (Q&A)
* Concept Explanation
* Quiz Generation
* Educational Text Summarization
* Personalized Learning Path Recommendations

The project uses **FastAPI** for the backend, **HTML, CSS, and JavaScript** for the frontend, and **Google Gemini API** for AI-powered learning functions.

---

## Features

### 1. Question & Answer

Students can ask academic questions and receive AI-generated answers with simple explanations.

### 2. Concept Explanation

EduGenie provides beginner-friendly explanations, examples, and important points for a given concept.

### 3. Quiz Generation

Students can select a topic and generate multiple-choice questions with four options and correct answers.

### 4. Summarization

Long educational passages can be summarized into simple, student-friendly key points for quick revision.

### 5. Learning Path Recommendation

EduGenie generates a structured learning path containing:

* Beginner fundamentals
* Intermediate concepts
* Advanced concepts
* Suggested duration
* Practice activities
* Small project ideas
* Weekly schedule
* Completion checklist

---

## Technology Stack

| Technology        | Purpose                                  |
| ----------------- | ---------------------------------------- |
| Python            | Backend development                      |
| FastAPI           | REST API framework                       |
| Google Gemini API | AI-powered learning functions            |
| HTML              | Web page structure                       |
| CSS               | Web page styling                         |
| JavaScript        | Frontend interaction and API integration |
| Uvicorn           | ASGI server                              |
| Jinja2            | HTML templating                          |
| python-dotenv     | Environment configuration                |
| Google GenAI SDK  | Gemini API integration                   |

## The current project setup uses **Python 3.14.4** and **Gemini 3.5 Flash-Lite**.

## System Workflow

```text
Student
   ↓
EduGenie Web Interface
   ↓
FastAPI Backend
   ↓
Google Gemini API
   ↓
AI-generated Result
   ↓
Student
```

The frontend sends task-specific POST requests to the FastAPI backend. The backend processes the request through the corresponding Python module and returns the AI-generated result to the web interface.

---

## Project Structure

```text
EduGenie-AI/
│
├── main.py
├── config.py
├── schemas.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── tests/
    ├── __init__.py
    └── test_app.py
```

---

## Backend API Endpoints

| Method | Endpoint                 | Purpose                            |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/`                      | Opens EduGenie web interface       |
| GET    | `/health`                | Checks backend status              |
| POST   | `/qa`                    | Answers student questions          |
| POST   | `/explain`               | Explains a concept                 |
| POST   | `/quiz`                  | Generates a quiz                   |
| POST   | `/summarize`             | Summarizes educational content     |
| POST   | `/learn/recommendations` | Generates learning recommendations |

---

## Web Interface

The EduGenie web interface contains:

* Task selection dropdown
* Student input textarea
* Quiz count selection
* Submit button
* AI result display area
* Check Answer interaction for quizzes
* Responsive CSS styling

The available tasks are **Explain, QnA, Quiz, Summary, and Recommend Path**.

---

## Live Integration

The frontend uses JavaScript `fetch()` to send POST requests to the FastAPI backend.

The AI-generated response is received from the backend and displayed directly on the web interface without manually refreshing the page.

---

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd EduGenie-AI
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_NEW_API_KEY
GEMINI_MODEL=gemini-3.5-flash-lite
USE_LOCAL_EXPLAINER=false
LOCAL_EXPLAINER_MODEL=MBZUAI/LaMini-Flan-T5-783M
MAX_INPUT_CHARS=12000
```

**Important:** Do not upload the `.env` file to GitHub because it contains the Gemini API key. Use `.env.example` for the public repository.

---

## Run the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

---

## Testing

The project includes tests for:

* Backend health endpoint
* Home page
* Empty-input validation

Run the tests using:

```bash
pytest
```

---

## Example Use Cases

### Q&A

A student asks:

```text
Which is the largest ocean?
```

EduGenie provides an AI-generated answer.

### Quiz

A student selects:

```text
Topic: Pythagoras Theorem
```

EduGenie generates multiple-choice questions.

### Learning Path

A student requests a learning path for:

```text
SQL
```

EduGenie generates a structured path from beginner to advanced concepts.

---

## Future Enhancements

Future versions of EduGenie can include:

* Voice-based interaction
* Multilingual support
* Mobile application
* Student progress tracking dashboards
* Gamification with badges and learning streaks
* Adaptive learning paths
* Group study sessions
* Teacher or parent dashboards
* Learning Management System integration
* Image and PDF input for doubt solving and summarization

---

## Conclusion

EduGenie combines a **FastAPI backend, web frontend, and Google Gemini AI** to provide an interactive learning assistant for students.

It supports question answering, concept explanation, quiz generation, summarization, and personalized learning recommendations. Its modular architecture also allows additional educational features to be added in the future.

---

## Project Status

**Project:** EduGenie – Google Gemini Powered Learning Assistant
**Backend:** FastAPI
**Frontend:** HTML, CSS, JavaScript
**AI Service:** Google Gemini API
**Status:** Functional Prototype

# Quickstart Guide: Textbook Generation Project

This guide provides instructions to quickly set up and run the AI-generated textbook project locally.

## Prerequisites

- Node.js 18 LTS or higher
- Python 3.11 or higher
- Git

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/physical-ai-textbook.git
cd physical-ai-textbook
```

## 2. Frontend Setup (Docusaurus)

Navigate to the Docusaurus project directory and install dependencies:

```bash
cd physical-ai-textbook
npm install
```

Create a `.env` file from the example and configure your backend API URL:

```bash
cp .env.example .env
# Edit .env with your backend API URL (e.g., VITE_BACKEND_URL=http://localhost:8000)
```

Start the Docusaurus development server:

```bash
npm start
```

Frontend runs at `http://localhost:3000`

## 3. Backend Setup (FastAPI)

Navigate to the FastAPI project directory:

```bash
cd rag_chatbot
```

Create a Python virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables for Qdrant and Neon credentials:

```bash
cp .env.example .env
# Edit .env with your Qdrant and Neon credentials
```

Initialize the PostgreSQL database (creates tables):

```bash
python scripts/setup_db.py
```

Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

Backend runs at `http://localhost:8000`

## 4. Index Chapters (for RAG Chatbot)

After starting the backend, index the textbook chapters into Qdrant and Neon:

```bash
cd rag_chatbot
python scripts/index_chapters.py
```

This will parse your Docusaurus markdown files, chunk them, embed them, and store them for the RAG chatbot.

## 5. Local Development Mock Server

For quick frontend development without full backend setup, you can use the mock FastAPI server:

```bash
cd rag_chatbot
python simple_server.py
```

This mock server runs at `http://localhost:8000` and provides placeholder responses for chat, personalization, and translation endpoints.

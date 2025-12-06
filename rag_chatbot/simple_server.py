import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="RAG Chatbot Mock Backend",
    description="A simple mock backend for local Docusaurus development.",
    version="1.0.0",
)

# Configure CORS for local Docusaurus development
origins = [
    "http://localhost:3000",  # Docusaurus frontend development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str
    selected_text: Optional[str] = None

class PersonalizationRequest(BaseModel):
    chapter_content: str
    user_background: dict

class TranslationRequest(BaseModel):
    chapter_content: str
    target_language: str

@app.get("/", tags=["Health Check"])
async def read_root():
    return {"message": "RAG Chatbot Mock Backend is running"}

@app.post("/chat")
async def mock_chat(request: ChatRequest):
    print(f"Mock Chat Request: Query='{request.query}', Selected Text='{request.selected_text}'")
    if request.selected_text:
        response = {"answer": f"Mock: Based on your selection '{request.selected_text}', Physical AI is about robots interacting with the world.", "sources": ["Mock Source: Selected Text"]
}
    elif "physical ai" in request.query.lower():
        response = {"answer": "Mock: Physical AI systems interact with the real world using sensors and actuators.", "sources": ["Mock Source: Intro to Physical AI"]
}
    elif "humanoid robotics" in request.query.lower():
        response = {"answer": "Mock: Humanoid robots are designed to mimic human form and movement.", "sources": ["Mock Source: Basics of Humanoid Robotics"]
}
    else:
        response = {"answer": "Mock: I'm a mock chatbot. I can provide basic info on Physical AI and Humanoid Robotics. Try asking about them!", "sources": []}
    return response

@app.post("/personalize")
async def mock_personalize(request: PersonalizationRequest):
    print(f"Mock Personalize Request: Content='{request.chapter_content[:50]}...', Background='{request.user_background}'")
    return {"personalized_content": f"Mock: This chapter content has been personalized for your {request.user_background.get("software_background", "general")} background."}

@app.post("/translate")
async def mock_translate(request: TranslationRequest):
    print(f"Mock Translate Request: Content='{request.chapter_content[:50]}...', Language='{request.target_language}'")
    if request.target_language == "ur":
        return {"translated_content": f"[ماک: اس باب کے مواد کا اردو ترجمہ: {request.chapter_content[:50]}...]"}
    else:
        return {"translated_content": f"Mock: Translation to {request.target_language} not supported."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

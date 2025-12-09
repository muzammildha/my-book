import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from physical_ai_textbook.chatbot import get_chatbot_response # Import the refactored function

app = FastAPI()

# Configure CORS to allow communication from your Docusaurus frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your Docusaurus frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessagePayload(BaseModel):
    thread_id: str | None = None # thread_id is not used by the current chatbot implementation
    user_message: str

class AssistantResponse(BaseModel):
    thread_id: str = "none" # Return a dummy thread_id as it's not used by the agent
    assistant_messages: list[str]

@app.post("/chat", response_model=AssistantResponse)
async def chat_with_assistant(payload: MessagePayload):
    try:
        response_text = await get_response_async(payload.user_message) # Call the async function
        return AssistantResponse(assistant_messages=[response_text])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

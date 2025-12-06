import pytest
from httpx import AsyncClient
from rag_chatbot.src.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "RAG Chatbot Backend is running"}

@pytest.mark.asyncio
async def test_chat_endpoint_physical_ai():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/chat", json={
            "query": "What is Physical AI?",
            "selected_text": None
        })
    assert response.status_code == 200
    assert "Physical AI" in response.json()["answer"]
    assert "sources" in response.json()

@pytest.mark.asyncio
async def test_chat_endpoint_selected_text():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/chat", json={
            "query": "Explain this:",
            "selected_text": "Physical AI refers to systems that interact with the real world."
        })
    assert response.status_code == 200
    assert "selected_text" in response.json()["answer"]
    assert "sources" in response.json()

@pytest.mark.asyncio
async def test_personalize_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/personalize", json={
            "chapter_content": "Introduction to Physical AI chapter content.",
            "user_background": {"software_background": "beginner", "hardware_background": "none"}
        })
    assert response.status_code == 200
    assert "personalized_content" in response.json()

@pytest.mark.asyncio
async def test_translate_endpoint_urdu():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/translate", json={
            "chapter_content": "Hello World!",
            "target_language": "ur"
        })
    assert response.status_code == 200
    assert "Urdu translation" in response.json()["translated_content"]

@pytest.mark.asyncio
async def test_translate_endpoint_unsupported_language():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/translate", json={
            "chapter_content": "Hello World!",
            "target_language": "fr"
        })
    assert response.status_code == 400
    assert "Unsupported target language" in response.json()["detail"]

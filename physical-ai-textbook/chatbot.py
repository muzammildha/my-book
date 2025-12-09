import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
import asyncio
from agents.run import RunConfig
from typing_extensions import TypedDict, Any
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
DOCS_PATH = os.path.join(os.getcwd(), "docs") # Assuming docs is in the same directory as chatbot.py

def load_and_chunk_docs():
    docs = []
    for p in Path(DOCS_PATH).rglob("*.mdx"):
        loader = UnstructuredMarkdownLoader(str(p))
        docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunked_docs = text_splitter.split_documents(docs)
    return chunked_docs

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.from_documents(load_and_chunk_docs(), embeddings)

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


@function_tool
async def fetch_weather(city:str) -> str:

    """Fetch the weather for a given location.

    Args:
        city: The city to fetch the weather for.
    """
    # In real life, we'd fetch the weather from a weather API
    return f"wheather is sunny in {city}"


@function_tool
async def get_sum(a:int,b:int)->str:
    """Get two integers and add it.

    Args:
        a: integer #1.
        b: integer #2.

    """
    return a+b

@function_tool
async def get_meaning(word: str, meaning: str) -> str:
    """Get a word and return its meaning."""
    return f"meaning of {word} is {meaning}"

async def get_response_async(prompt: str) -> str:
    result = await Runner.run(agent, prompt, run_config=config)
    return result.final_output



agent = Agent(
    name="Nextjs agent",
    instructions="You are a helpful next js agent guides developer",
    tools=[fetch_weather, get_sum, get_meaning]
)

def get_chatbot_response(prompt: str) -> str:
    result = Runner.run_sync(agent, prompt, run_config=config)
    return result.final_output

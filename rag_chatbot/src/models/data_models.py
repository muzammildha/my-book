from pydantic import BaseModel
from typing import List, Dict, Optional

class UserProfile(BaseModel):
    id: str
    software_background: str
    hardware_background: str

class ChapterContent(BaseModel):
    chapter_id: str
    title: str
    content: str
    metadata: Dict = {}

class Chunk(BaseModel):
    id: str
    chapter_id: str
    content: str
    embedding: List[float]
    metadata: Dict = {}

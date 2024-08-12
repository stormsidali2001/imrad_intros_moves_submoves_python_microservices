from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional


class SentenceClass:
    sentence: str
    move: int
    subMove: int


class ClassBasedSummary(BaseModel):
    class_based_summary: str = Field(
        description="A summary taking into consideration and mensioning the switching between the IMRAD introduction moves and submoves"
    )

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional

from pydantic import BaseModel as BaseModelV2


class SentenceClass(BaseModelV2):
    sentence: str = Field(description="The sentence text")
    move: int = Field(description="The imrad introduction move")
    subMove: int = Field(description="The imrad introduction subMove")


class ClassBasedSummary(BaseModel):
    class_based_summary: str = Field(
        description="A summary taking into consideration and mensioning the switching between the IMRAD introduction moves and submoves"
    )

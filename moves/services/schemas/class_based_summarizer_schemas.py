from langchain_core.pydantic_v1 import BaseModel, Field

from pydantic import BaseModel as BaseModelV2
from typing import List


class SentenceClass(BaseModelV2):
    sentence: str = Field(description="The sentence text")
    move: int = Field(description="The imrad introduction move")
    subMove: int = Field(description="The imrad introduction subMove")


class ClassBasedSummaryCreatedEventDto(BaseModelV2):
    introductionId: str
    content: str


class ClassBasedSummaryEventDto(BaseModelV2):
    introductionId: str
    content: List[SentenceClass]


class ClassBasedSummary(BaseModel):
    class_based_summary: str = Field(
        description="A summary taking into consideration and mensioning the switching between the IMRAD introduction moves and submoves. This field text should be beautifly markdown formated and easy to ready and follow.Use line breaks when switching between sections"
    )

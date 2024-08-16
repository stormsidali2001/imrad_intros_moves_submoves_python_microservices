from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel as BaseModelV2


class GlobalSummaryEventDto(BaseModelV2):
    introductionId: str
    content: str


class Summary(BaseModel):
    content: str = Field(
        description="The global summary of the Imrad introduction.This field text should be beautifly markdown formated and easy to ready and follow."
    )
    problimatic: str = Field(
        description="The problematic which was introduced by the author"
    )

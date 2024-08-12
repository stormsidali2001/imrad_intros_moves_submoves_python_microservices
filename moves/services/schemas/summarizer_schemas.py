from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    content: str = Field(
        description="The global summary of the Imrad introduction, should not take more than 4 lines"
    )
    problimatic: str = Field(
        description="The problematic which was introduced by the author"
    )

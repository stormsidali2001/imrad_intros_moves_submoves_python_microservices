from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate


from .llm_model import model
from services.schemas.summarizer_schemas import Summary


print("init model-----------------------------")


print("file indexer here .........................")
parser = PydanticOutputParser(pydantic_object=Summary)


prompt = PromptTemplate(
    template="Given this IMRAD introduction. Summarize it without loosing the main informations and findings into 3 lines at most.\n {introduction}\n {format_instructions}.",
    input_variables=["introduction"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt | model | parser
# chain =  RunnableParallel(
#    completion=complete_chain, prompt_value=prompt
# ) | RunnableLambda(lambda x: retry_parser.parse_with_prompt(**x))


def summarize_introduction(introduction: str) -> Summary:
    return chain.invoke({"introduction": introduction})

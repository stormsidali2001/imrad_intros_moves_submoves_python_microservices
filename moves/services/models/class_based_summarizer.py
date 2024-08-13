from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

# load envs
from .llm_model import model
from services.schemas.class_based_summarizer_schemas import ClassBasedSummary


print("init model-----------------------------")


print("file indexer here .........................")
parser = PydanticOutputParser(pydantic_object=ClassBasedSummary)


prompt = PromptTemplate(
    template="Given this IMRAD introduction sentences with their corresponding classes.Explain the author thought process.\n Mension the IMRAD move and submoves when switching between two different moves or submoves sections .\n {sentences}\n {format_instructions}",
    input_variables=["sentences"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt | model | parser
# chain =  RunnableParallel(
#    completion=complete_chain, prompt_value=prompt
# ) | RunnableLambda(lambda x: retry_parser.parse_with_prompt(**x))


def summarize_sentences_with_classes(sentences: str) -> ClassBasedSummary:
    return chain.invoke({"sentences": sentences})

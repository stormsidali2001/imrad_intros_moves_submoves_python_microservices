from langchain_google_genai import ChatGoogleGenerativeAI

# load envs
from dotenv import load_dotenv
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache


load_dotenv()

# os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

print("init model-----------------------------")
model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    timeout=None,
    max_retries=3,
)
set_llm_cache(InMemoryCache())

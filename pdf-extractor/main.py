from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse
import PyPDF2
import re


from py_eureka_client.eureka_client import EurekaClient
from contextlib import asynccontextmanager

eureka_server_url = "http://0.0.0.0:8761"


@asynccontextmanager
async def startup(app: FastAPI):
    client = EurekaClient(
        eureka_server=eureka_server_url, app_name="pdf_extractor", instance_port=8010
    )
    await client.start()
    yield


app = FastAPI(lifespan=startup)


# Download NLTK data if not already downloaded
def extract_introduction(content: str) -> str:
    # Define the heuristic map for section starts
    section_map = {
        "introduction": [
            "INTRODUCTION",
            #
        ],
        "next_section": [
            r"\d+\.\s*[A-Z][a-z]*",  # Matches patterns like "2. Overview" or "1. Methods"
            "METHODS",
            #
            "METHODOLOGY",
            #
            "EXPERIMENTS",
            #
            "OVERVIEW",
            #
            "RESULTS",
            #
            "DISCUSSION",
            #
            "CONCLUSION",
            #
            "RELATED WORK",
            #
        ],
    }

    # Compile the regex patterns
    intro_start_pattern = re.compile(
        r"\b(?:" + "|".join(section_map["introduction"]) + r")\b"
    )
    next_section_pattern = re.compile(
        r"\b(?:" + "|".join(section_map["next_section"]) + r")\b"
    )

    # Search for the start of the introduction
    intro_start_match = intro_start_pattern.search(content)
    if not intro_start_match:
        return "Introduction section not found."

    intro_start_index = intro_start_match.end()
    print("Start index : " + str(intro_start_index))
    print("example " + content[intro_start_index : intro_start_index + 100])

    # Search for the start of the next section after the introduction
    next_section_match = next_section_pattern.search(content, intro_start_index)
    intro_end_index = next_section_match.start() if next_section_match else len(content)

    print("End index : " + str(intro_end_index))

    # Extract the introduction content
    introduction_content = content[intro_start_index:intro_end_index].strip()

    return introduction_content


@app.post("/extract_introduction")
async def extract_introduction_endpoint(file: UploadFile = File(...)):
    """Extracts the introduction from an uploaded PDF file."""

    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)

    return await process_pdf(file.filename)


async def process_pdf(pdf_source):
    # Process the PDF from URL or local file
    file = open(pdf_source, "rb")

    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text() + " \n "

    file.close()

    return {
        "status": "Processing completed",
        "text": text,
        "introduction": extract_introduction(text),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8010)

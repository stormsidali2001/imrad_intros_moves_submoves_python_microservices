from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from py_eureka_client.eureka_client import EurekaClient
from contextlib import asynccontextmanager
import requests
from services.summarizers import (
    summarize_imrad_sentences_with_classes,
    summarize_introduction,
)
from services.redis.subscribers import (
    init_global_summary_creation_subscriber,
    init_class_based_summary_creation_subscriber,
)
from services.schemas.class_based_summarizer_schemas import SentenceClass
from typing import List
import asyncio


eureka_server_url = "http://0.0.0.0:8761"

model_id_url = {
    "moves": "http://0.0.0.0:8501/v1/models/moves:predict",
    "sub_moves_0": "http://0.0.0.0:8501/v1/models/sub_moves_0:predict",
    "sub_moves_1": "http://0.0.0.0:8501/v1/models/sub_moves_1:predict",
    "sub_moves_2": "http://0.0.0.0:8501/v1/models/sub_moves_2:predict",
}


async def get_predictions(model_url: str, sentences: list[str] = []):
    response = requests.post(model_url, None, {"instances": sentences})
    print("status code -------------------------")
    print(response.status_code)
    if response.status_code != 200:
        raise Exception("Error in prediction")

    json = response.json()

    if "predictions" not in json:
        raise Exception("Error in prediction")

    predictions = json["predictions"]
    return [
        {"class": int(np.argmax(x)), "probability": float(np.max(x))}
        for i, x in enumerate(predictions)
    ]


async def start_subscribers():
    # This will run the subscriber loop in the background
    asyncio.create_task(init_global_summary_creation_subscriber())
    asyncio.create_task(init_class_based_summary_creation_subscriber())


@asynccontextmanager
async def startup(app: FastAPI):
    client = EurekaClient(
        eureka_server=eureka_server_url, app_name="ai_model_moves", instance_port=8000
    )
    await client.start()
    await start_subscribers()

    yield
    # Shutdown code here


def on_error(err_type: str, err: Exception):
    print("----------------------------")
    print(err_type, err, sep=": ")


app = FastAPI(lifespan=startup)
origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

# connect with eureka client


@app.post("/summary/generate")
async def generate_summary(introduction: str):
    print("----------------")
    print("introduction")
    print(introduction)
    return summarize_introduction(introduction)


@app.post("/summary/class-based/generate")
async def generate_class_based_summary(sentences: List[SentenceClass]):
    print("Invoking class based generation")
    print(sentences)
    return summarize_imrad_sentences_with_classes(sentences)


@app.post("/models/{id}/predict/batch")
async def predict_batch(sentences: list[str], id: str):
    model_url = model_id_url[id]
    if not model_url:
        return Exception("Model not found")

    print("prediction started....")
    predictions = await get_predictions(model_url, sentences)

    # map to a list of dicts with the class and the probability
    print(predictions)
    return predictions


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import tensorflow as tf
import tensorflow_text as text
import keras

#import tensorflow_text as text
from fastapi.encoders import jsonable_encoder
import json
import numpy as np


from py_eureka_client.eureka_client import EurekaClient
from contextlib import asynccontextmanager
eureka_server_url = "http://0.0.0.0:8761"

model_id_path_map = {
    "moves": "model_data_moves",
    "sub_moves_0": "model_data_0_submoves",
    "sub_moves_1": "model_data_1_submoves",
    "sub_moves_2": "model_data_2_submoves",
    
}


models = {
    "moves": None,
    "sub_moves_0": None,
    "sub_moves_1": None,
    "sub_moves_2": None,
}

async def load_models():
    print("loading models ...")
    for key in  model_id_path_map.keys():
        models[key] = keras.models.load_model(model_id_path_map[key])
        print(f"Model {key} loaded")



tf.get_logger().setLevel('ERROR')
moves_classification_model_path = 'model_epoch_2'; 





@asynccontextmanager
async def startup(app: FastAPI):
    
    client = EurekaClient(eureka_server=eureka_server_url, app_name="ai_model_moves", instance_port=8000)
    await client.start()
    await load_models()
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
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

# connect with eureka client


@app.post("/models/{id}/predict/batch")
async def predict_batch(sentences: list[str], id:str):
    model = models[id]
    if not model:
        return   Exception("Model not found")

    print("prediction started....")
    predictions = model.predict(sentences)
    # map to a list of dicts with the class and the probability
    predictions  = [{'class':int(np.argmax(x)),'probability':float(np.max(x))} for i,x in enumerate(predictions)]
    print(predictions)
    return predictions 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
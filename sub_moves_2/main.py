from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import tensorflow as tf
import keras

#import tensorflow_text as text
from fastapi.encoders import jsonable_encoder
import json
import numpy as np




from py_eureka_client.eureka_client import EurekaClient
from contextlib import asynccontextmanager
eureka_server_url = "http://172.23.16.1:8761"



print(keras.__version__)

tf.get_logger().setLevel('ERROR')
moves_classification_model_path = 'model_data_2_submoves'; 




model = None

@asynccontextmanager
async def startup(app: FastAPI):
    client = EurekaClient(eureka_server=eureka_server_url, app_name="ai_model_moves_2", instance_port=8003)
    await client.start()
    yield
    # Shutdown code here
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

@app.get("/")
async def root():
    return {"message": "Hello World"}

print("loading model")
model = keras.models.load_model(moves_classification_model_path)
print("loading model completed.......")



@app.post("/predict/batch")
async def predict_batch(sentences: list[str]):
    print("prediction started....")
    predictions = model.predict(sentences)
    predictions = model.predict(sentences)
    predictions  = [{'class':int(np.argmax(x)),'probability':float(np.max(x))} for i,x in enumerate(predictions)]
    print(predictions)

    return predictions 

    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
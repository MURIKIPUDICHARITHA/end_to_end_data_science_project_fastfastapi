
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model/model.pkl")

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Model Prediction"}

@app.post("/predict")
def predict(data: InputData):
    input_features = np.array([[data.feature1, data.feature2]])
    prediction = model.predict(input_features)
    return {"prediction": prediction.tolist()}

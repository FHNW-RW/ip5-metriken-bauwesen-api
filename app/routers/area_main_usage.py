import time

from fastapi import APIRouter
from joblib import load

from app.routers.models import HNFPredictionInputs, PredictionResult
from app.routers import transformer

router = APIRouter(prefix="/hauptnutzflaeche")
model = load('models/linear_reg_model.joblib')


@router.post("/predict", response_model=PredictionResult, tags=["Hauptnutzfläche"])
async def predict(inputs: HNFPredictionInputs):
    start = time.time()

    input_df = transformer.transform(inputs)
    prediction = model.predict(input_df)[0]

    exec_time = round((time.time() - start), 3)

    return PredictionResult(prediction=prediction, exec_time=exec_time)

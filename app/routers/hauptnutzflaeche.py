from typing import Final

from fastapi import APIRouter
from joblib import load

from app.models import HNFPredictionInputs, PredictionResult
from app.routers import transformer

MODEL_TYPE: Final = 'GradientBoosting'

# load serialized model/pipeline
model = load('data/models/hnf_gb_model.joblib')
pipeline = load('data/pipelines/hnf_pipeline.joblib')

router = APIRouter(prefix='/hnf')


@router.post('/predict', response_model=PredictionResult, summary='Schätzen der Hauptnutzfläche (HNF)', tags=['Hauptnutzfläche'])
async def predict(inputs: HNFPredictionInputs):
    input_df = transformer.transform(pipeline, inputs)
    prediction = model.predict(input_df)[0]

    return PredictionResult(prediction=prediction, model=MODEL_TYPE)

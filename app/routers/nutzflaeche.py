from typing import Final

from fastapi import APIRouter
from joblib import load

from app.models import PredictionResult, NFPredictionInputs
from app.routers import transformer

MODEL_TYPE: Final = 'GradientBoosting'

# TODO: use real model & pipeline for nf
# load serialized model/pipeline
model = load('models/nf_gb_model.joblib')
pipeline = load('transformer/nf_pipeline.joblib')

router = APIRouter(prefix='/nf')


@router.post('/predict', response_model=PredictionResult, summary='Schätzen der Nutzfläche (NF)', tags=['Nutzfläche'])
async def predict(inputs: NFPredictionInputs):
    input_df = transformer.transform(pipeline, inputs)
    prediction = model.predict(input_df)[0]

    return PredictionResult(prediction=prediction, model=MODEL_TYPE)

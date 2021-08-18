from typing import Final

from fastapi import APIRouter
from joblib import load

from app.models import PredictionResult, NFPredictionInputs
from app.routers import transformer

MODEL_TYPE: Final = 'GradientBoosting'

# load serialized model/pipeline
model = load('data/models/nf_gb_model.joblib')
pipeline = load('data/pipelines/nf_pipeline.joblib')

router = APIRouter(prefix='/nf')


@router.post('/predict', response_model=PredictionResult, summary='Schätzen der Nutzfläche (NF)', tags=['Nutzfläche'])
async def predict(inputs: NFPredictionInputs):
    input_df = transformer.transform(pipeline, inputs)
    prediction = model.predict(input_df)[0]

    return PredictionResult(prediction=prediction, model=MODEL_TYPE)

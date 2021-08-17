from typing import Final

from fastapi import APIRouter
from joblib import load

from app.models import GFPredictionInputs, PredictionResult
from app.routers import transformer

MODEL_TYPE: Final = 'GradientBoosting'

# load serialized model/pipeline
model = load('data/models/gf_gb_model.joblib')
pipeline = load('data/pipelines/gf_pipeline.joblib')

router = APIRouter(prefix='/gf')


@router.post('/predict', response_model=PredictionResult, summary='Schätzen der Geschossfläche (GF)', tags=['Geschossfläche'])
async def predict(inputs: GFPredictionInputs):
    input_df = transformer.transform(pipeline, inputs)
    prediction = model.predict(input_df)[0]

    return PredictionResult(prediction=prediction, model=MODEL_TYPE)

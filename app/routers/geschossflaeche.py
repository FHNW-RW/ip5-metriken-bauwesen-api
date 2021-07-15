from fastapi import APIRouter
from joblib import load

from app.models import HNFPredictionInputs, PredictionResult
from app.routers import transformer

model = load('models/fitted_model.joblib')
pipeline = load('transformer/fitted_pipeline.joblib')

router = APIRouter(prefix='/gf')


@router.post('/predict', response_model=PredictionResult, tags=['Geschossfläche'])
async def predict(inputs: HNFPredictionInputs):
    input_df = transformer.transform(pipeline, inputs)
    prediction = model.predict(input_df)[0]

    return PredictionResult(prediction=prediction)

import time

import pandas as pd

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic.main import BaseModel
from joblib import load


router = APIRouter(prefix="/hauptnutzflaeche")
model = load('models/linear_reg_model.joblib')


class HNFPredictionInputs(BaseModel):
    area_total_floor_416: int
    area_main_usage: int


@router.post("/predict/")
async def predict(inputs: HNFPredictionInputs):
    start = time.time()

    # convert json to pandas dataframe
    inputs_dict = jsonable_encoder(inputs)
    for key, value in inputs_dict.items():
        inputs_dict[key] = [value]

    input_df = pd.DataFrame.from_dict(inputs_dict)
    prediction = model.predict(input_df)[0]

    exec_time = round((time.time() - start), 3)

    return {
        "prediction": prediction,
        "exec_time": exec_time,
    }

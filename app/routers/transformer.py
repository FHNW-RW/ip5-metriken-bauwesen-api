from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from joblib import load
from pandas import DataFrame

from app.routers.models import HNFPredictionInputs

usage_encoder = load('encoders/usage_encoder.joblib')


def transform(inputs: HNFPredictionInputs) -> DataFrame:
    try:
        df = DataFrame(jsonable_encoder(inputs), index=[0])
        df['usage_cluster'] = usage_encoder.transform(df['usage_cluster'])
    except BaseException as e:
        raise HTTPException(status_code=400, detail=f"Error while transforming dataset. Exception=[{str(e)}]")

    return df

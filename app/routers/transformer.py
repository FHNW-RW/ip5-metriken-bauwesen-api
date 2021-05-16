from fastapi.encoders import jsonable_encoder
from pandas import DataFrame

from app.routers.models import HNFPredictionInputs


def transform(inputs: HNFPredictionInputs) -> DataFrame:
    df = DataFrame(jsonable_encoder(inputs), index=[0])

    # todo: transform data to fit trained model
    df['area_main_usage'] = 0

    return df

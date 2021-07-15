from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pandas import DataFrame


def transform(pipeline, inputs) -> DataFrame:
    try:
        df = DataFrame(jsonable_encoder(inputs), index=[0])
        df = pipeline.transform(df)
    except BaseException as e:
        raise HTTPException(status_code=400, detail=f"Error while transforming dataset. Exception=[{str(e)}]")

    return df

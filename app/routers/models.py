from pydantic.main import BaseModel


class PredictionResult(BaseModel):
    prediction: float
    exec_time: float


class HNFPredictionInputs(BaseModel):
    area_total_floor_416: int
    area_main_usage: str

from pydantic.main import BaseModel


class PredictionResult(BaseModel):
    prediction: float


class HNFPredictionInputs(BaseModel):
    area_total_floor_416: int
    total_expenses: int
    volume_total_416: int
    volume_total_116: int
    usage_cluster: str


class GFPredictionInputs(BaseModel):
    area_main_usage: int
    total_expenses: int
    volume_total_416: int
    volume_total_116: int
    usage_cluster: str

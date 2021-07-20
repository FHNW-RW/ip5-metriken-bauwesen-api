from pydantic.main import BaseModel


class PredictionResult(BaseModel):
    prediction: float
    model: str


class GeneralPredictionInputs(BaseModel):
    usage_cluster: str
    total_expenses: int
    volume_total_416: int
    volume_total_116: int
    num_floors_underground: int
    num_floors_overground: int
    garage_combined: float
    primary_usage_percentage: float


class HNFPredictionInputs(GeneralPredictionInputs):
    area_total_floor_416: int


class GFPredictionInputs(GeneralPredictionInputs):
    area_main_usage: int


class NFPredictionInputs(GeneralPredictionInputs):
    area_total_floor_416: int

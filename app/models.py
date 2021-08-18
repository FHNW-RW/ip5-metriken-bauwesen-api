from pydantic import BaseModel, Field


class PredictionResult(BaseModel):
    prediction: float = Field(None, title='Schätzung')
    model: str = Field(None, title='Verwendetes Modell')


class GeneralPredictionInputs(BaseModel):
    usage_cluster: str = Field(None, title='Cluster der Hauptnutzung')
    total_expenses: int = Field(None, title='Gesamtkosten')
    volume_total_416: float = Field(None, title='Volumen SIA 416')
    volume_total_116: float = Field(None, title='Volumen SIA 116')
    num_floors_underground: int = Field(None, title='Anzahl unterirdischer Stockwerke')
    num_floors_overground: int = Field(None, title='Anzahl oberirdischer Stockwerke')
    garage_combined: float = Field(None, title='Anteil aller Garagen')
    primary_usage_percentage: float = Field(None, title='Anteil des primären Nutzungstyp')


class HNFPredictionInputs(GeneralPredictionInputs):
    area_total_floor_416: int = Field(None, title='Geschossfläche GF')


class GFPredictionInputs(GeneralPredictionInputs):
    area_main_usage: int = Field(None, title='Hauptnutzfläche HNF')


class NFPredictionInputs(GeneralPredictionInputs):
    area_total_floor_416: int = Field(None, title='Geschossfläche GF')

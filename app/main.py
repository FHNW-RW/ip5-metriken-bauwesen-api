from fastapi import FastAPI

from .routers import hauptnutzflaeche
from .routers import geschossflaeche
from .routers import nutzflaeche

app = FastAPI(
    title="Metriken im Bauwesen",
    version="1.0",
    description="API zum Schätzen verschiedener Metriken im Bauwesen.",
)

app.include_router(hauptnutzflaeche.router)
app.include_router(geschossflaeche.router)
app.include_router(nutzflaeche.router)

from fastapi import FastAPI

from .routers import hauptnutzflaeche
from .routers import geschossflaeche

app = FastAPI(
    title="Metriken im Bauwesen",
    version="1.0",
    description="API zum Schätzen verschiedener Metriken im Bauwesen.",
)

app.include_router(hauptnutzflaeche.router)
app.include_router(geschossflaeche.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

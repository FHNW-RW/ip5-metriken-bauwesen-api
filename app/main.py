from fastapi import FastAPI

from .routers import area_main_usage

app = FastAPI(
    title="Metriken im Bauwesen",
    version="1.0",
    description="API zum Schätzen verschiedener Metriken im Bauwesen.",
)

app.include_router(area_main_usage.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

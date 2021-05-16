from fastapi import APIRouter

router = APIRouter(prefix="/hauptnutzflaeche")


@router.get("/predict")
async def predict():
    return {"message": "Hello World"}

from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger

from modules.calcul import calcul

app = FastAPI(title="M5B1 API")


class NumberIn(BaseModel):
    value: int


class NumberOut(BaseModel):
    result: int


@app.get("/")
def root():
    return {"message": "M5B1 API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/calcul", response_model=NumberOut)
def compute(payload: NumberIn):
    logger.info(f"calcul({payload.value})")
    return NumberOut(result=calcul(payload.value))

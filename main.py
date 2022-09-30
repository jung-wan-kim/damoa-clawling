from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import damoa

app = FastAPI()


@app.get("/")
def read_root():
    window_id = damoa.phoneAuth()
    return {"window_id": window_id}


class Item(BaseModel):
    name: str


@app.post("/items/{window_id}")
def read_item(window_id: str, item: Item):
    damoa.updateSerInfo(window_id, item.name)
    return {'result': 'ok'}

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    debug=True,
    version="0.1.0",
    title="FastAPI test",
    description="This is a test of the FastAPI framework",
    contact={
        "name": "Fabien Bellanger",
        "url": "https://fabien-bellanger.fr",
    },
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/", name="Root")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

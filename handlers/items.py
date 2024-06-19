from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel


# Models
"""
Item model

@author Fabien Bellanger
"""


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

    """
    Display item
    
    Display the name and the price of an item.
    """

    def display(self) -> str:
        return self.name + " at " + str(self.price)


# Items router
router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={404: {"description": "Page Not found"}},
    include_in_schema=True,
)


@router.get("/{item_id}")
def read_item(item_id: int, q: Union[bool, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item": item.display(), "item_id": item_id}

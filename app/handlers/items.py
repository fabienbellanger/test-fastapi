from fastapi import APIRouter
from pydantic import BaseModel


# Models
class _Item(BaseModel):
    """
    Item model (Private)

    @author Fabien Bellanger
    """

    name: str
    price: float
    is_offer: bool | None = None

    def display(self) -> str:
        """
        Display item

        Display the name and the price of an item.
        """

        return self.name + " at " + str(self.price)


# Items router
router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={404: {"description": "Page Not found"}},
    include_in_schema=True,
)


@router.get("/{item_id}")
def read_item(item_id: int, q: bool | None = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
def update_item(item_id: int, item: _Item):
    return {"item": item.display(), "item_id": item_id}

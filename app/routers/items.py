from fastapi import APIRouter
from app.schemas.item import ItemBase


router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={404: {"description": "Page Not found"}},
    include_in_schema=True,
)


@router.get("/{item_id}", description="Get item from its ID")
async def read_item(item_id: int, q: bool | None = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}", description="Update item from its ID")
async def update_item(item_id: int, item: ItemBase):
    return {"item": item.display(), "item_id": item_id}

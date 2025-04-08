from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.schemas.item import Item, ItemEdit
from app.repositories import item as item_repository
from . import get_db, check_token

router = APIRouter(
    tags=["Items"],
    responses={
        401: {"description": "Unauthorized"},
        404: {"description": "Resource Not found"},
    },
    include_in_schema=True,
    dependencies=[Depends(check_token)],
)


@router.get(
    "/{item_id}",
    response_model=Item,
    description="Get item from its ID",
    summary="Get item",
)
async def get_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = item_repository.get_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get(
    "/",
    response_model=list[Item],
    description="List all items",
    summary="Get all items",
)
async def get_all_items(db: Session = Depends(get_db)):
    items = item_repository.get_items(db)
    return items


@router.post(
    "/", response_model=Item, description="Create an item", summary="Create an item"
)
async def create_item(item: ItemEdit, db: Session = Depends(get_db)):
    db_item = item_repository.create_item(db, item=item)
    if db_item is None:
        raise HTTPException(status_code=500, detail="Error during item creation")
    return db_item

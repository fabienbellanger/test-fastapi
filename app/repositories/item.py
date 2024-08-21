from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemEdit


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session):
    return db.query(Item).all()


def create_item(db: Session, item: ItemEdit):
    db_item = Item(name=item.name, price=item.price, is_offer=item.is_offer)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

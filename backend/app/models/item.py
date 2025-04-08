from sqlalchemy import Boolean, Column, Integer, String, Float
from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=False)
    price = Column(Float, index=False)
    is_offer = Column(Boolean)

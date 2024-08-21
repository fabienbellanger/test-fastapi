from sqlalchemy import Column, String, DateTime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    lastname = Column(String, index=False, nullable=False)
    firstname = Column(String, index=False, nullable=False)
    created_at = Column(DateTime, index=False, nullable=False)

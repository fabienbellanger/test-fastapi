from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from sqlalchemy.orm import Session

from . import get_db
from app.repositories import user as user_repo
from app.schemas.user import LoginResponse, LoginRequest


router = APIRouter(
    tags=["Auth"],
    responses={
        401: {"description": "Unauthorized"},
        404: {"description": "Resource Not found"},
    },
    include_in_schema=True,
)


@router.post("/login", response_model=LoginResponse, description="Login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> LoginResponse:
    req = LoginRequest(username=form_data.username, password=form_data.password)
    db_login = user_repo.login(db, req)
    if db_login is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return db_login

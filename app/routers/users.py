from fastapi import Depends, APIRouter, status, HTTPException
from typing import Annotated

from sqlalchemy.orm import Session

from . import check_token, get_db
from app.schemas.user import UserResponse, Payload
from app.repositories import user as user_repo


router = APIRouter(
    tags=["Users"],
    responses={
        401: {"description": "Unauthorized"},
        404: {"description": "Resource Not found"},
    },
    include_in_schema=True,
)


@router.get("/me", response_model=UserResponse, description="Read users me")
async def read_users_me(
    payload: Annotated[Payload, Depends(check_token)],
    db: Session = Depends(get_db),
):
    db_user = user_repo.get_by_id(db, payload.user_id)
    user = UserResponse(
        id=db_user.id,
        username=db_user.username,
        lastname=db_user.lastname,
        firstname=db_user.firstname,
        created_at=str(db_user.created_at),
    )

    return user


@router.get("/", response_model=list[UserResponse], description="List all users")
async def get_all(
    _=Depends(check_token),
    db: Session = Depends(get_db),
):
    try:
        db_users = user_repo.get_all(db)
        users = list(
            map(
                lambda db_user: UserResponse(
                    id=db_user.id,
                    username=db_user.username,
                    lastname=db_user.lastname,
                    firstname=db_user.firstname,
                    # created_at=str(db_user.created_at),
                ),
                db_users,
            )
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error during users fetching",
        )

    return users

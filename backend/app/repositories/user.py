from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.config import JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ALGORITHM, JWT_SECRET_KEY
from app.schemas.user import LoginRequest, LoginResponse
from app.models.user import User
from app.security.password import Password
from app.security.token import JwtToken


def login(db: Session, req: LoginRequest):
    password = Password()

    db_user = db.query(User).filter(User.username == req.username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found",
        )
    if not password.verify_password(req.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    # Generate token
    token = JwtToken(
        algorithm=JWT_ALGORITHM,
        secret_key=JWT_SECRET_KEY,
        expires_duration=JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    access_token = token.create_access_token(
        {
            "sub": db_user.username,
            "user_id": db_user.id,
        }
    )

    return LoginResponse(
        id=db_user.id,
        username=db_user.username,
        lastname=db_user.lastname,
        firstname=db_user.firstname,
        created_at=str(db_user.created_at),
        access_token=access_token,
        token_type="bearer",
    )


def get_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def get_all(db: Session):
    return db.query(User).all()

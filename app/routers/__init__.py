from typing import Annotated

from fastapi import Depends

from app.config import JWT_ALGORITHM, JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRE_MINUTES
from app.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer

from app.schemas.user import LoginRequest
from app.security.token import JwtToken

# Security - OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


async def check_token(token: Annotated[LoginRequest, Depends(oauth2_scheme)]):
    jwt_token = JwtToken(
        algorithm=JWT_ALGORITHM,
        secret_key=JWT_SECRET_KEY,
        expires_duration=JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    )

    return jwt_token.decode_access_token(token)


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

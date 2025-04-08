from datetime import timedelta, timezone, datetime

import jwt
from fastapi import HTTPException, status
from jwt import InvalidTokenError

from app.schemas.user import Payload


class JwtToken:
    _algorithm: str
    _secret_key: str
    _expires_duration: float

    def __init__(self, algorithm: str, secret_key: str, expires_duration: float):
        self._algorithm = algorithm
        self._secret_key = secret_key
        self._expires_duration = expires_duration

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self._expires_duration)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._secret_key, algorithm=self._algorithm)

        return encoded_jwt

    def decode_access_token(self, token: str) -> Payload:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            payload = jwt.decode(token, self._secret_key, algorithms=[self._algorithm])
            username: str = payload.get("sub")
            user_id: str = payload.get("user_id")

            if username is None:
                raise credentials_exception

            res = Payload(user_id=user_id, username=username)
        except InvalidTokenError:
            raise credentials_exception

        return res

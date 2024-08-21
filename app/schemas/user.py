from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: str
    username: str
    lastname: str
    firstname: str
    created_at: str


class UserResponse(User):
    pass


class LoginResponse(User):
    access_token: str
    token_type: str


class Payload(BaseModel):
    user_id: str
    username: str

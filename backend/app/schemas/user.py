from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., description="Username of the user")
    password: str = Field(..., description="Password of the user")


class User(BaseModel):
    id: str = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")
    lastname: str = Field(..., description="Lastname of the user")
    firstname: str = Field(..., description="Firstname of the user")
    created_at: str = Field(..., description="Date when the user was created")


class UserResponse(User):
    pass


class LoginResponse(User):
    access_token: str = Field(..., description="Access token")
    token_type: str = Field(..., description="Token type")


class Payload(BaseModel):
    user_id: str = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")

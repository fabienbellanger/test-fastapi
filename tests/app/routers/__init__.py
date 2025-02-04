from fastapi import status
from tests import client


def get_access_token(username: str, password: str) -> str:
    response = client.post(
        "/api/v1/login",
        data={"username": username, "password": password},
    )
    assert response.status_code == status.HTTP_200_OK

    token = response.json().get("access_token")
    assert token is not None

    return token

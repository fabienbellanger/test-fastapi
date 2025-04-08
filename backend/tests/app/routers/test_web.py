from fastapi import status
from tests import client


def test_home():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Hello": "World"}


def test_hello():
    response = client.get("/hello/Fabien")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Hello, Fabien!"


def test_health():
    response = client.get("/health")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_not_found():
    response = client.get("/sdfsfs")
    assert response.status_code == status.HTTP_404_NOT_FOUND

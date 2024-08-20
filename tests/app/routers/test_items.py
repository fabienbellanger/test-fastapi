from fastapi import status
from tests import client

# Get item


def test_get_item():
    response = client.get("/api/v1/items/5")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"item_id": 5, "q": None}


def test_get_item_query_parameter():
    response = client.get("/api/v1/items/5?q=true")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"item_id": 5, "q": True}

    response = client.get("/api/v1/items/5?q=0")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"item_id": 5, "q": False}
    assert response.headers["content-type"] == "application/json"


def test_get_item_invalid_query_parameter():
    response = client.get("/api/v1/items/5?q=89")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_get_item_invalid_item():
    response = client.get("/api/v1/items/str")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


# Update item


def test_put_item():
    response = client.put(
        "/api/v1/items/5", json={"name": "item", "price": 10.5, "is_offer": True}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"item": "item at 10.5", "item_id": 5}

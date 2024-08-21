from fastapi import status
from tests import client

# Get item


def test_get_item():
    response = client.post(
        "/api/v1/items", json={"name": "Test", "price": 10.5, "is_offer": True}
    )
    assert response.status_code == status.HTTP_200_OK

    item_id = response.json().get("id")
    response = client.get("/api/v1/items/" + str(item_id))
    assert response.json() == {"id": 1, "name": "Test", "price": 10.5, "is_offer": True}


def test_get_item_not_found():
    response = client.get("/api/v1/items/123456789")
    assert response.status_code == status.HTTP_404_NOT_FOUND


# Create an item


def test_create_item():
    response = client.post(
        "/api/v1/items", json={"name": "Test", "price": 10.5, "is_offer": True}
    )
    assert response.status_code == status.HTTP_200_OK

    item = response.json()
    assert item.get("name") == "Test"
    assert item.get("price") == 10.5
    assert item.get("is_offer") == True

from fastapi import status
from tests import client
from tests.app.routers import get_access_token

# Get item


def test_get_item():
    token = get_access_token("fabien", "fabien")

    response = client.post(
        "/api/v1/items",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Test", "price": 10.5, "is_offer": True},
    )
    assert response.status_code == status.HTTP_200_OK

    item_id = response.json().get("id")
    response = client.get(
        "/api/v1/items/" + str(item_id),
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.json() == {
        "id": item_id,
        "name": "Test",
        "price": 10.5,
        "is_offer": True,
    }


def test_get_item_not_found():
    token = get_access_token("fabien", "fabien")

    response = client.get(
        "/api/v1/items/123456789", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


# Create an item


def test_create_item():
    token = get_access_token("fabien", "fabien")

    response = client.post(
        "/api/v1/items",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Test", "price": 10.5, "is_offer": True},
    )
    assert response.status_code == status.HTTP_200_OK

    item = response.json()
    assert item.get("name") == "Test"
    assert item.get("price") == 10.5
    assert item.get("is_offer") == True

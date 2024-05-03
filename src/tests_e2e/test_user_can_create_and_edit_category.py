import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCreateAndEditCategory:
    def test_user_can_create_and_edit_category(self) -> None:
        api_client  = APIClient()

        # Verifica que lista esta vazia
        list_response = api_client.get("/api/categories/")
        assert list_response.data == {"data": []}

        # Cria uma categoria
        create_response = api_client.post("/api/categories/",
                                          {"name": "Movie", "description": "Movie description"})
        assert create_response.status_code == 201
        created_category_id = create_response.data["id"]

        # Verifica que a categoria foi criada
        list_response = api_client.get("/api/categories/")
        assert list_response.data == {
            "data": [
                {
                    "id": created_category_id,
                    "name": "Movie",
                    "description": "Movie description",
                    "is_active": True
                }
            ]
        }

        # Edita a categoria criada
        edit_response = api_client.put(f"/api/categories/{created_category_id}/",
                                       {"name": "Serie", "description": "Serie description", "is_active": True})
        assert edit_response.status_code == 204

        # Verifica que a categoria foi editada
        updated_category = api_client.get(f"/api/categories/{created_category_id}/")
        assert updated_category.data == {
            "data": {
                "id": created_category_id,
                "name": "Serie",
                "description": "Serie description",
                "is_active": True
            }
        }

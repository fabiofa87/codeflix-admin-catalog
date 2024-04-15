import uuid
from uuid import UUID, uuid4

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.category.domain.category import Category
from django_project.category_app.repository import DjangoORMCategoryRepository


@pytest.fixture
def category_repository() -> DjangoORMCategoryRepository:
    return DjangoORMCategoryRepository()


@pytest.fixture
def category_movie():
    return Category(
        name="Movie",
        description="Movie description",
    )


@pytest.fixture
def category_serie():
    return Category(
        name="Serie",
        description="Serie description",
    )


@pytest.mark.django_db
class TestCategoryAPI:
    def test_when_id_is_invalid_return_bad_request(self, category_repository: DjangoORMCategoryRepository):
        url = "/api/categories/invalid_id/"
        response = APIClient().get(url)

        assert response.status_code == 400

    def test_list_categories(self,
                             category_repository: DjangoORMCategoryRepository,
                             category_movie: Category,
                             category_serie: Category):
        category_repository.save(category_movie)
        category_repository.save(category_serie)

        url = "/api/categories/"
        response = APIClient().get(url)

        expected_data = [
            {
                "id": str(category_movie.id),
                "name": category_movie.name,
                "description": category_movie.description,
                "is_active": True
            },
            {
                "id": str(category_serie.id),
                "name": category_serie.name,
                "description": category_serie.description,
                "is_active": True
            }
        ]

        assert response.status_code == 200
        assert response.json() == expected_data
        assert len(response.data) == 2


@pytest.mark.django_db
class TestRetrieveAPI:
    def test_return_category_when_exists(self,
                                         category_movie: Category,
                                         category_serie: Category,
                                         category_repository: DjangoORMCategoryRepository,
                                         ):
        category_repository.save(category_movie)
        category_repository.save(category_serie)

        url = f"/api/categories/{category_movie.id}/"
        response = APIClient().get(url)

        expected_data = {
            "id": str(category_movie.id),
            "name": "Movie",
            "description": "Movie description",
            "is_active": True
        }

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_data

    def test_return_404_when_category_not_exists(self):
        random_id = str(uuid.uuid4())

        url = f"/api/categories/{random_id}/"
        response = APIClient().get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND


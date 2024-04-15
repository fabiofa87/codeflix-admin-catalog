import pytest
from rest_framework.test import  APIClient

from core.category.domain.category import Category
from django_project.category_app.repository import DjangoORMCategoryRepository


@pytest.mark.django_db
class TestCategoryAPI:
    @pytest.fixture
    def category_repository(self) -> DjangoORMCategoryRepository:
        return DjangoORMCategoryRepository()

    @pytest.fixture
    def category_movie(self):
        return Category(
            name="Movie",
            description="Movie description",
        )

    @pytest.fixture
    def category_serie(self):
        return Category(
            name="Serie",
            description="Serie description",
        )

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


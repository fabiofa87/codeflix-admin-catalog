from rest_framework.test import APITestCase

from core.category.domain.category import Category
from django_project.category_app.repository import DjangoORMCategoryRepository


class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        category_movie = Category(
            name="Movie",
            description="Movie description",
        )
        category_serie = Category(
            name="Serie",
            description="Serie description",
        )

        repository = DjangoORMCategoryRepository()
        repository.save(category_movie)
        repository.save(category_serie)

        url = "/api/categories/"
        response = self.client.get(url)

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

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

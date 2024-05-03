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
class TestListAPI:
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

        expected_data = {
            "data":
                [
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
                ]}

        assert response.status_code == 200
        assert response.json() == expected_data
        assert len(response.data["data"]) == 2


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

        expected_data = {"data":
                             {"id": str(category_movie.id),
                              "name": "Movie",
                              "description": "Movie description",
                              "is_active": True}
                         }

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_data

    def test_return_404_when_category_not_exists(self) -> None:
        random_id = str(uuid4())

        url = f"/api/categories/{random_id}/"
        response = APIClient().get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestCreateAPI:
    def test_when_payload_is_invalid_and_return_400(self) -> None:
        url = "/api/categories/"
        response = APIClient().post(
            url,
            data={
                "name": "",
                "description": "Movie description",
            }
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"name": ["This field may not be blank."]}

    def test_when_payload_is_valid_return_201(self, category_repository: DjangoORMCategoryRepository) -> None:
        url = "/api/categories/"
        response = APIClient().post(
            url,
            data={
                "name": "Movie",
                "description": "Movie description",
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"]

        saved_category = category_repository.get_by_id(response.data["id"])
        assert saved_category == Category(
            id=UUID(response.data["id"]),
            name="Movie",
            description="Movie description",
            is_active=True,
        )


@pytest.mark.django_db
class TestUpdateAPI:
    def test_when_payload_is_invalid_and_return_400(self) -> None:
        url = f"/api/categories/1234556/"
        response = APIClient().put(
            url,
            data={
                "name": "",
                "description": "Movie description",
            }
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            "name": ["This field may not be blank."],
            "id": ["Must be a valid UUID."],
            "is_active": ["This field is required."]
        }

    def test_when_payload_is_valid_return_200(self, category_movie: Category,
                                              category_repository: DjangoORMCategoryRepository) -> None:
        category_repository.save(category_movie)
        url = f"/api/categories/{category_movie.id}/"
        response = APIClient().put(
            url,
            data={
                "name": "Movie",
                "description": "Movie description",
                "is_active": True
            },

        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

        expected_category = Category(
            id=category_movie.id,
            name="Movie",
            description="Movie description",
            is_active=True
        )

        updated_category = category_repository.get_by_id(category_movie.id)

        for (key, value) in expected_category.__dict__.items():
            assert getattr(updated_category, key) == value

    def test_when_category_not_exists_return_404(self) -> None:
        random_id = str(uuid4())

        url = f"/api/categories/{random_id}/"
        response = APIClient().put(
            url,
            data={
                "name": "Movie",
                "description": "Movie description",
                "is_active": True
            },

        )

        assert response.status_code == status.HTTP_404_NOT_FOUND

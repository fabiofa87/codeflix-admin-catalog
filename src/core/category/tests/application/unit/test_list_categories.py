from unittest.mock import create_autospec
from src.core.category.application.use_cases.list_category import ListCategory, ListCategoryRequest, ListCategoryResponse, CategoryOutput
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category


class TestListCategories:
    def test_when_no_categories_in_repository_return_empty_list(self):
        category = Category(name="Filme", description="Categoria de filmes")
        repository = create_autospec(CategoryRepository)
        repository.get_all.return_value = []

        use_case = ListCategory(repository=repository)
        request = ListCategoryRequest()

        response = use_case.execute(request)

        assert response == ListCategoryResponse(
            data=[]
        )

    def test_when_categories_in_repository_return_list(self):
        category_filme = Category(name="Filme", description="Categoria de filmes")
        category_serie = Category(name="Serie", description="Categoria de series")

        repository = create_autospec(CategoryRepository)
        repository.get_all.return_value = [category_filme, category_serie]

        use_case = ListCategory(repository=repository)
        request = ListCategoryRequest()

        response = use_case.execute(request)

        assert response == ListCategoryResponse(
            data=[
                CategoryOutput(
                    id=category_filme.id,
                    name=category_filme.name,
                    description=category_filme.description,
                    is_active=category_filme.is_active
                ),
                CategoryOutput(
                    id=category_serie.id,
                    name=category_serie.name,
                    description=category_serie.description,
                    is_active=category_serie.is_active
                )
            ]
        )
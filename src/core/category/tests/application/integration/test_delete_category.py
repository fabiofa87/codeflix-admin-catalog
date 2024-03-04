
import uuid
import pytest
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestDeleteCategory:
    def test_delete_existing_category(self):
        category_filme = Category(name="Filme", description="Categoria de filmes")
        category_series = Category(name="Séries", description="Categoria de séries")

        repository = InMemoryCategoryRepository(categories=[category_filme, category_series])
        use_case = DeleteCategory(repository)

        request = DeleteCategoryRequest(category_filme.id)
        use_case.execute(request)

        assert repository.get_by_id(category_filme.id) is None

    def test_when_category_not_exist_raise_exception(self):
        category_filme = Category(name="Filme", description="Categoria de filmes")
        category_series = Category(name="Séries", description="Categoria de séries")

        repository = InMemoryCategoryRepository(categories=[category_filme, category_series])
        use_case = DeleteCategory(repository)
        request = DeleteCategoryRequest(uuid.uuid4())

        with pytest.raises(CategoryNotFound) as exc:
            use_case.execute(request)
        assert str(exc.value) == f"Category with id {request.id} not found"



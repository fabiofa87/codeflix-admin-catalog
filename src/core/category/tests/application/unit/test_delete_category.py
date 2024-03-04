from unittest.mock import create_autospec
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category


class TestDeleteCategory:
    def test_delete_category(self):
        category = Category(name="Filme", description="Categoria de filmes")

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value(category.id)

        use_case = DeleteCategory(repository=mock_repository)

        request = DeleteCategoryRequest(id=category.id)
        use_case.execute(request)

        mock_repository.delete.assert_called_once_with(category.id)

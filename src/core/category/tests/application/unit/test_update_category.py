from unittest.mock import create_autospec

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_update_category_name(self):
        category = Category(name="Movie", description="Movie category description", is_active=True)
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, name="Movie 2")

        use_case.execute(request)

        assert category.name == "Movie 2"
        assert category.description == "Movie category description"
        mock_repository.update.assert_called_once_with(category)

    def test_update_description(self):
        category = Category(name="Movie", description="Movie category description", is_active=True)
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, description="Some description")

        use_case.execute(request)

        assert category.name == "Movie"
        assert category.description == "Some description"
        mock_repository.update.assert_called_once_with(category)


    def test_can_activate_category(self):
        category = Category(name="Movie", description="Movie category description", is_active=True)
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, is_active=False)

        use_case.execute(request)

        assert category.name == "Movie"
        assert category.description == "Movie category description"
        assert category.is_active == True
        mock_repository.update.assert_called_once_with(category)

    def test_can_deactivate_category(self):
        category = Category(name="Movie", description="Movie category description", is_active=False)
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, is_active=True)

        use_case.execute(request)

        assert category.name == "Movie"
        assert category.description == "Movie category description"
        assert category.is_active == False
        mock_repository.update.assert_called_once_with(category)
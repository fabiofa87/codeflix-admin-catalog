from unittest.mock import MagicMock
from uuid import UUID

import pytest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import InvalidcategoryData

from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest



class TestCreateCategory:
    def test_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(mock_repository)
        request = CreateCategoryRequest(name="Filme", description="Filme description", is_active=True)

        category_id = use_case.execute(request)

        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mock_repository.save.called is True

    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(mock_repository)
        request = CreateCategoryRequest(name="")


        with pytest.raises(InvalidcategoryData, match="name cannot be empty") as exc_info:
            category_id = use_case.execute(request)
        assert exc_info.type is InvalidcategoryData
        assert str(exc_info.value) == "name cannot be empty"



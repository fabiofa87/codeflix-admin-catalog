import pytest
from uuid import UUID

from src.core.category.domain.category import Category


class TestCategory:
    def test_name_is_required(self):
        with pytest.raises(TypeError, match= "missing 1 required positional argument: 'name'"):
            Category()

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Test")
        assert isinstance(category.id, UUID)


    def test_created_category_must_be_created_with_default_values(self):
        category = Category(name="Test")
        assert category.id is not None
        assert category.is_active == True
        assert category.description == ""
        assert category.name == "Test"

    def test_name_must_have_less_than_255_chars(self):
        with pytest.raises(ValueError, match="name must have less than 255 characters"):
            Category(name="a" * 256)

    def test_name_cannot_be_empty(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")

    def test_category_can_be_deactivated(self):
        category = Category(name="Test")
        category.deactivate()
        assert category.is_active == False

    def test_category_can_be_activated(self):
        category = Category(name="Test", is_active=False)
        category.activate()
        assert category.is_active == True

class TestUpdateCategory:
    def test_update_category_with_invalid_name(self):
        category = Category(name="Test movie", description="Test for a cool movie")

        with pytest.raises(ValueError, match="name must have less than 255 characters"):
            category.update_category(name="a" * 256, description="Test for a cool movie")
    
    def test_update_category_with_empty_name(self):
        category = Category(name="Test movie", description="Test for a cool movie")

        with pytest.raises(ValueError, match="name cannot be empty"):
            category.update_category(name="", description="Test for a cool movie")

    

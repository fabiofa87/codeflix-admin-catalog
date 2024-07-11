import pytest
from uuid import UUID

from src.core.category.domain.category import Category
from src.core.genre.domain.genre import Genre


class TestGenre:
    def test_create_genre_with_default_values(self):
        genre = Genre(name="Action")
        assert genre.name == "Action"
        assert genre.is_active == True
        assert genre.categories == set()
        assert isinstance(genre.id, UUID)

    def test_name_must_have_less_than_255_chars(self):
        with pytest.raises(ValueError, match="name must have less than 255 characters"):
            Genre(name="a" * 256)

    def test_name_cannot_be_empty(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Genre(name="")

    def test_genre_can_be_deactivated(self):
        genre = Genre(name="Action")
        genre.deactivate()
        assert genre.is_active == False

    def test_genre_can_be_activated(self):
        genre = Genre(name="Action", is_active=False)
        genre.activate()
        assert genre.is_active == True


    def test_add_category_to_genre(self):
        genre = Genre(name="Action")
        category = Category(name="FPS")
        genre.add_category(category)
        assert category in genre.categories

    

class TestUpdateGenre:
    def test_update_genre_with_invalid_name(self):
        genre = Genre(name="Action")

        with pytest.raises(ValueError, match="name must have less than 255 characters"):
            genre.update_genre(name="a" * 256, is_active=True)

    def test_update_genre_with_empty_name(self):
        genre = Genre(name="Action", is_active=True)

        with pytest.raises(ValueError, match="name cannot be empty"):
            genre.update_genre(name="", is_active=True)

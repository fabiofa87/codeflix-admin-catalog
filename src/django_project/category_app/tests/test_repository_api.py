import pytest
from src.django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.category_app.models import Category as CategoryModel
from src.core.category.domain.category import Category


@pytest.mark.django_db
class TestSave:
    def test_saves_category_in_database(self):
        category = Category(
            name="Movie",
            description="Movie description",
        )
        repository = DjangoORMCategoryRepository()

        assert CategoryModel.objects.count() == 0
        repository.save(category)
        assert CategoryModel.objects.count() == 1

        category_db = CategoryModel.objects.get()
        assert category_db.id == category.id
        assert category_db.name == category.name
        assert category_db.description == category.description
        assert category_db.is_active == category.is_active

    def test_list_categories_from_db(self):
        category = Category(
            name="Movie",
            description="Movie description",
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        assert repository.get_all() == [category]

    def test_get_category_by_id(self):
        category = Category(
            name="Movie",
            description="Movie description",
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        assert repository.get_by_id(category.id) == category

    def test_update_category(self):
        category = Category(
            name="Movie",
            description="Movie description",
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        category.name = "Film"
        category.description = "Film description"
        repository.update(category)
        assert repository.get_by_id(category.id) == category

    def test_delete_category(self):
        category = Category(
            name="Movie",
            description="Movie description",
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        repository.delete(category.id)
        assert repository.get_by_id(category.id) is None

from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestInMemoryCategoryReposittry:
    def test_can_save_category(self):
        repository = InMemoryCategoryRepository()
        category = Category(name="Filme", description="Filme description")

        repository.save(category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category


    def test_get_category_by_id(self):
        repository = InMemoryCategoryRepository()
        category = Category(name="Filme", description="Filme description")
        repository.save(category)

        result = repository.get_by_id(category.id)

        assert result == category

    def test_delete_category(self):
        category = Category(name="Filme", description="Filme description")
        repository = InMemoryCategoryRepository(categories=[category])

        repository.delete(category.id)

        assert len(repository.categories) == 0
        assert repository.get_by_id(category.id) is None

    def test_update_category(self):
        category = Category(name="Filme", description="Filme description")
        repository = InMemoryCategoryRepository(categories=[category])

        category.name = "Filme 2"
        category.description = "Filme description 2"

        repository.update(category)

        assert len(repository.categories) == 1
        assert repository.categories[0].name == "Filme 2"
        assert repository.categories[0].description == "Filme description 2"
        assert repository.categories[0].is_active == True
        assert repository.get_by_id(category.id).name == "Filme 2"
        assert repository.get_by_id(category.id).description == "Filme description 2"
        assert repository.get_by_id(category.id).is_active == True
        assert repository.get_by_id(category.id) == category
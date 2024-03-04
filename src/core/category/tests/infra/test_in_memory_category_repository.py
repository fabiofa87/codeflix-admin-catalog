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
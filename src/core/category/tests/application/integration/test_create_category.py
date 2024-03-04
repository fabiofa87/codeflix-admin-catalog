
from uuid import UUID
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest



class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository()
        use_case = CreateCategory(repository)
        request = CreateCategoryRequest(name="Filme", description="Categoria para filmes")

        response = use_case.execute(request)


        assert response is not None
        assert isinstance(response.id, UUID)
        assert len(repository.categories) == 1
        
        persisted_category = repository.categories[0]
        assert persisted_category.name == "Filme"

        persisted_category_id = response.id
        assert persisted_category.id == persisted_category_id

        persisted_description = "Categoria para filmes"
        assert persisted_category.description == persisted_description

        persisted_is_active = True
        assert persisted_category.is_active == persisted_is_active
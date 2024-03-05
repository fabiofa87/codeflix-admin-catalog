from src.core.category.application.use_cases.update_category import UpdateCategoryRequest, UpdateCategory
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_can_update_category_name_and_description(self):
        category = Category(name="Movie", description="Movie category description", is_active=True)
        
        category_repository = InMemoryCategoryRepository()
        category_repository.save(category)

        use_case = UpdateCategory(repository=category_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="Movie 2",
            description="Some description"
        )

        use_case.execute(request)

        category = category_repository.get_by_id(category.id)

        assert category.name == "Movie 2"
        assert category.description == "Some description"
        assert category.is_active == True

        
        
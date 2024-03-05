from src.core.category.application.use_cases.list_category import CategoryOutput, ListCategoryResponse, ListCategory, ListCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestListCategories:
    def test_return_empty_list(self):
        
        repository = InMemoryCategoryRepository(categories=[])
        

        use_case = ListCategory(repository=repository)
        request = ListCategoryRequest()

        response = use_case.execute(request)

        assert response == ListCategoryResponse(
            data=[]
        )

    def test_return_list_with_content(self):
        category_filme = Category(name="Filme", description="Categoria de filmes")
        category_serie = Category(name="Serie", description="Categoria de series")

        repository = InMemoryCategoryRepository(categories=[category_filme, category_serie])

        use_case = ListCategory(repository=repository)
        request = ListCategoryRequest()

        response = use_case.execute(request)

        assert response == ListCategoryResponse(
            data=[
                CategoryOutput(
                    id=category_filme.id,
                    name=category_filme.name,
                    description=category_filme.description,
                    is_active=category_filme.is_active
                ),
                CategoryOutput(
                    id=category_serie.id,
                    name=category_serie.name,
                    description=category_serie.description,
                    is_active=category_serie.is_active
                )
            ]
        )
from src.core.category.domain.category_repository import CategoryRepository


class DjangoORMCategoryRepository(CategoryRepository):
    def __init__(self, category_model: CategoryModel):
        self.category_model = category_model
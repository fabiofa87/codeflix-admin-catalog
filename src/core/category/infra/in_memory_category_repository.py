from uuid import UUID
from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)

    def get_by_id(self, id: UUID) -> Category | None:
        category_id = [category for category in self.categories if category.id == id]
        if category_id:
            return category_id[0]
        return None
    
    def delete(self, id: UUID) -> None:
        category = self.get_by_id(id)
        self.categories.remove(category)

    def update(self, category: Category) -> None:
        category = self.get_by_id(id)
        category = category
        self.save(category)
        
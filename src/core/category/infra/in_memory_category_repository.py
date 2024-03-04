from src.core.category.application.category_repository import CategoryRepository


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)

    def get_by_id(self, id):
        category_id = [category for category in self.categories if category.id == id]
        if category_id:
            return category_id[0]
        return None
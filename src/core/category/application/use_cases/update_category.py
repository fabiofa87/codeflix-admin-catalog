from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository


@dataclass
class UpdateCategoryRequest:
    id: UUID
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None
    

class UpdateCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository


    def execute(self, request: UpdateCategoryRequest):
        category = self.repository.get_by_id(request.id)
        current_name = category.name
        current_description = category.description
        
        if request.name is not None:
            current_name = request.name

        if request.description is not None:
            current_description = request.description
        
        if request.is_active:
            category.deactivate()
        
        if request.is_active is False:
            category.activate()

        category.update_category(name=current_name, description=current_description)

        self.repository.update(category)
        
    
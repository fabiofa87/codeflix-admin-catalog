import uuid
from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class Genre:
    name: str
    is_active: bool = True
    categories: set[UUID] = field(default_factory=set)
    id: UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        self.validate()

    def __eq__(self, other):  # a == b -> a.__eq__(b)
        if not isinstance(other, Genre):
            return False

        return self.id == other.id

    def activate(self):
        self.is_active = True
        self.validate()

    def deactivate(self):
        self.is_active = False
        self.validate()

    def update_genre(self, name: str, is_active: bool, categories: set[UUID] = set()):
        self.name = name
        self.is_active = is_active
        self.categories = categories

        self.validate()

    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name must have less than 255 characters")

        if len(self.name) == 0:
            raise ValueError("name cannot be empty")
        return self

    def add_category(self, category_id: uuid.UUID):
        self.categories.add(category_id)
        self.validate()

    def remove_category(self, category_id: uuid.UUID):
        self.categories.remove(category_id)
        self.validate()

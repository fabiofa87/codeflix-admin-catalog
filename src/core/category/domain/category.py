from dataclasses import dataclass, field
import uuid

@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    
    def __post_init__(self):
        self.validate()
        

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id
    
    def update_category(self, name, description):
        self.name = name
        self.description = description
        
        self.validate()
        return self
    
    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name must have less than 255 characters")

        if len(self.name) == 0:
            raise ValueError("name cannot be empty")
        return self
    
    def activate(self):
        self.is_active = True
        self.validate()
        return self
    
    def deactivate(self):
        self.is_active = False
        self.validate()
        return self
from abc import ABC, abstractmethod
from uuid import UUID

from core.genre.domain.genre import Genre




class GenreRepository(ABC):
    @abstractmethod
    def save(self, category)-> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: UUID) -> Genre | None:
        raise NotImplementedError
    
    @abstractmethod
    def get_all(self) -> list[Genre]:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, genre: Genre) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, genre: Genre) -> None:
        raise NotImplementedError
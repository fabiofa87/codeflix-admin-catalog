from dataclasses import dataclass, field
from uuid import UUID
from core.genre.application.use_cases.exceptions import InvalidGenreData
from core.genre.domain.genre import Genre
from src.core.genre.domain.genre_repository import GenreRepository


@dataclass
class CreateGenreRequest:
    name: str
    categories: list[str] = field(default_factory=list)
    is_active: bool = True

@dataclass
class CreateGenreResponse:
    id: UUID

class CreateGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    def execute(self, request: CreateGenreRequest) -> CreateGenreResponse:
        try:
            genre = Genre(name=request.name, categories=request.categories, is_active=request.is_active)
        except ValueError as error:
            raise InvalidGenreData(error)
        
        self.repository.save(genre)

        return CreateGenreResponse(id=genre.id)
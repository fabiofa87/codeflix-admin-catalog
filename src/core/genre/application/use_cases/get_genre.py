from dataclasses import dataclass

from core.genre.application.use_cases.exceptions import GenreNotFound
from core.genre.domain.genre_repository import GenreRepository


@dataclass
class GetGenreRequest:
    id: int

@dataclass
class GetGenreResponse:
    id: int
    name: str
    categories: list
    is_active: bool

class GetGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    def execute(self, request: GetGenreRequest) -> GetGenreResponse:
        genre = self.repository.get_by_id(request.id)

        if(genre is None):
            raise GenreNotFound(f'Genre with id {request.id} not found')

        return GetGenreResponse(
            id=genre.id,
            name=genre.name,
            categories=genre.categories,
            is_active=genre.is_active
        )
from dataclasses import dataclass

from core.genre.application.use_cases.exceptions import GenreNotFound
from core.genre.domain.genre_repository import GenreRepository


@dataclass
class DeleteGenreRequest:
    id: int

class DeleteGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    def execute(self, request: DeleteGenreRequest) -> None:
        if self.repository.get_by_id(request.id) is None:
            raise GenreNotFound(f'Genre with id {request.id} not found')

        self.repository.delete(request.id)
from dataclasses import dataclass

from core.genre.domain.genre_repository import GenreRepository


@dataclass
class ListGenreRequest:
    pass

@dataclass
class GenreOutput:
    id: int
    name: str
    categories: list
    is_active: bool

@dataclass
class ListGenreResponse:
    data: list[GenreOutput]


class ListGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    def execute(self, request: ListGenreRequest) -> ListGenreResponse:
        genres = self.repository.get_all()
        
        return ListGenreResponse(
            data=[GenreOutput(
                id=genre.id,
                name=genre.name,
                categories=genre.categories,
                is_active=genre.is_active
            ) for genre in genres]
        )
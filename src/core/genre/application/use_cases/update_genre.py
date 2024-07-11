from dataclasses import dataclass

from core.genre.application.use_cases.exceptions import GenreNotFound, InvalidGenre
from core.genre.domain import genre
from core.genre.domain.genre_repository import GenreRepository


@dataclass
class UpdateGenreRequest:
    id: int
    name: str | None
    categories: list | None = None
    is_active: bool | None = None

class UpdateGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    def execute(self, request: UpdateGenreRequest) -> None:
        genre = self.repository.get_by_id(request.id)

        if genre is None:
            raise GenreNotFound(f"Genre with {request.id} not found")

        try:
                if request.is_active is True:
                    genre.activate()

                if request.is_active is False:
                    genre.deactivate()

                current_name = genre.name
                current_categories = genre.categories

                if request.name is not None:
                    current_name = request.name

                if request.categories is not None:
                    current_categories = request.categories

                genre.update_genre(name=current_name, categories=current_categories)

        except ValueError as e:
            raise InvalidGenre(str(e)) from e
        
        self.repository.update(genre)

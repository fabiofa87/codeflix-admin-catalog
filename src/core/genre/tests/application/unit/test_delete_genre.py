from unittest.mock import create_autospec
from core.genre.application.use_cases.delete_genre import DeleteGenre, DeleteGenreRequest
from core.genre.domain.genre import Genre
from core.genre.domain.genre_repository import GenreRepository


class TestDeleteGenre:
    def test_delete_genre(self):
        genre = Genre(name="Action")

        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value(genre.id)

        use_case = DeleteGenre(repository=mock_repository)

        request = DeleteGenreRequest(id=genre.id)
        use_case.execute(request)

        mock_repository.delete.assert_called_once_with(genre.id)


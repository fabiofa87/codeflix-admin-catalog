from unittest.mock import MagicMock
from core.genre.application.use_cases.create_genre import CreateGenre, CreateGenreRequest
from src.core.genre.domain.genre_repository import GenreRepository
from uuid import UUID

class TestCreateGenre:
    def test_create_genre(self):
        mock_repository = MagicMock(GenreRepository)
        use_case = CreateGenre(mock_repository)
        request = CreateGenreRequest(name="Action", is_active=True)

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True

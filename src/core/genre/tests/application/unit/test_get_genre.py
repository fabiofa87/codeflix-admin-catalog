from unittest.mock import create_autospec
from core.category.domain.category import Category
from core.genre.application.use_cases.get_genre import GetGenre, GetGenreRequest, GetGenreResponse
from core.genre.domain.genre import Genre
from core.genre.domain.genre_repository import GenreRepository


class TestGetGenre:
    def test_get_genre_by_id(self):
        genre = Genre(name="Action")
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = genre

        use_case = GetGenre(repository=mock_repository)

        request = GetGenreRequest(id=genre.id)

        response = use_case.execute(request)

        assert response == GetGenreResponse(
            id=genre.id,
            name=genre.name,
            is_active=True,
            categories=set()
        )

    def test_get_genre_with_categories(self):
        genre = Genre(name="Action")
        category = Category(name="Filme", description="Categoria de filmes")
        genre.add_category(category.id)

        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = genre

        use_case = GetGenre(repository=mock_repository)

        request = GetGenreRequest(id=genre.id)

        response = use_case.execute(request)

        assert response == GetGenreResponse(
            id=genre.id,
            name=genre.name,
            is_active=True,
            categories={category.id}
        )

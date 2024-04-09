from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK

from core.category.application.use_cases.list_category import ListCategoryRequest, ListCategory
from django_project.category_app.repository import DjangoORMCategoryRepository


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        input = ListCategoryRequest()
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        output = use_case.execute(input)

        categories = [{
            "id": str(category.id),
            "name": category.name,
            "description": category.description,
            "is_active": category.is_active
        } for category in output.data]

        return Response(status=HTTP_200_OK, data=categories)

    def retrieve(self, request, pk=None):
        pass

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

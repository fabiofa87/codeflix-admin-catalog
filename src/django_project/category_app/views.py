from uuid import UUID

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from core.category.application.use_cases.exceptions import CategoryNotFound
from core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from core.category.application.use_cases.list_category import ListCategoryRequest, ListCategory
from django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.category_app.serializers import ListCategoryResponseSerializer, RetrieveCategoryRequestSerializer, \
    CategoryResponseSerializer


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        input = ListCategoryRequest()
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        output = use_case.execute(input)

        serializer = ListCategoryResponseSerializer(instance=output)

        return Response(status=HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        serializer = RetrieveCategoryRequestSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)

        use_case = GetCategory(repository=DjangoORMCategoryRepository())

        try:
            result = use_case.execute(request=GetCategoryRequest(id=serializer.validated_data["id"]))
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)

        category_output = CategoryResponseSerializer(instance=result)

        return Response(status=HTTP_200_OK, data=category_output.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

from uuid import UUID

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, \
    HTTP_204_NO_CONTENT

from core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from core.category.application.use_cases.exceptions import CategoryNotFound, InvalidcategoryData
from core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from core.category.application.use_cases.list_category import ListCategoryRequest, ListCategory
from django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.category_app.serializers import ListCategoryResponseSerializer, RetrieveCategoryRequestSerializer, \
    CategoryResponseSerializer, CreateCategoryRequestSerializer, CreateCategoryResponseSerializer, \
    RetrieveCategoryResponseSerializer

from src.core.category.application.use_cases.update_category import UpdateCategoryRequest, UpdateCategory
from src.django_project.category_app.serializers import UpdateCategoryRequestSerializer


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        input = ListCategoryRequest()
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        output = use_case.execute(input)

        serializer = ListCategoryResponseSerializer(instance=output)

        return Response(status=HTTP_200_OK, data=serializer.data)

    def retrieve(self, request: Request, pk=None):
        serializer = RetrieveCategoryRequestSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)

        use_case = GetCategory(repository=DjangoORMCategoryRepository())

        try:
            result = use_case.execute(request=GetCategoryRequest(id=serializer.validated_data["id"]))
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)

        category_output = RetrieveCategoryResponseSerializer(instance=result)

        return Response(status=HTTP_200_OK, data=category_output.data)

    def create(self, request: Request) -> Response:
        serializer = CreateCategoryRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        input = CreateCategoryRequest(**serializer.validated_data)

        use_case = CreateCategory(repository=DjangoORMCategoryRepository())

        result = use_case.execute(request=input)

        return Response(
            status=HTTP_201_CREATED,
            data=CreateCategoryResponseSerializer(result).data,
        )

    def update(self, request: Request, pk=None) -> Response:
        serializer = UpdateCategoryRequestSerializer(data=
                                                     {
                                                         **request.data,
                                                         "id": pk
                                                     })
        serializer.is_valid(raise_exception=True)

        input = UpdateCategoryRequest(**serializer.validated_data)

        use_case = UpdateCategory(repository=DjangoORMCategoryRepository())

        try:
            use_case.execute(request=input)
        except CategoryNotFound:
            return Response(
                status=HTTP_404_NOT_FOUND
            )

        return Response(
            status=HTTP_204_NO_CONTENT
        )

    def partial_update(self, request: Request, pk=None):
        pass

    def destroy(self, request: Request, pk=None):
        pass

from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .serializers import AuthorSerializer

from .services.create import CreateAuthorService
from .services.all_authors import ListAllAuthorsService
from .services.get_author import OneAuthorService
from .services.updated_author import UpdatedAuthorService
from .services.delete import DeleteAuthorService
from utils.pagination import Pagination


class AuthorListAPIView(APIView):

    def get(self, request):
        queryset = ListAllAuthorsService.service()
        return Pagination.paginate(queryset, request, AuthorSerializer)

    def post(self, request):
        return CreateAuthorService.service(request)


class AuthorDetailAPIView(APIView):
    def get(self, request, pk):
        return OneAuthorService.service(pk)

    def patch(self, request, pk):
        return UpdatedAuthorService.service(pk, request.data)

    def delete(self, request, pk):
        return DeleteAuthorService.service(pk)

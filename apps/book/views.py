from rest_framework.views import APIView

from .serializers import BookSerializer

from .services.all_books import ListAllBooksService
from .services.get_book import OneBookService
from .services.create import CreateBookService
from .services.updated_book import UpdatedBookService
from .services.delete import DeleteBookService

from utils.pagination import Pagination


class BookListAPIView(APIView):

    def get(self, request):
        queryset = ListAllBooksService.service()
        return Pagination.paginate(queryset, request, BookSerializer)

    def post(self, request):
        return CreateBookService.service(request)

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        return OneBookService.service(pk)
    
    def patch(self, request, pk):
        return UpdatedBookService.service(pk, request.data)
    
    def delete(self, request, pk):
        return DeleteBookService.service(pk)

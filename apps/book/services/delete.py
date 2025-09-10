from rest_framework.response import Response
from rest_framework import status

from ..models import Book

class DeleteBookService:
    @staticmethod
    def service(pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Response({"data": "Nook not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        book.is_active = False
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
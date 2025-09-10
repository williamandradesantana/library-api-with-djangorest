from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from ..serializers import BookSerializer
from ..models import Book

class UpdatedBookService:
    @staticmethod
    def service(book_id, book_data):
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            return Response({"data": "Book not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=book_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from ..models import Book
from ..serializers import BookSerializer


class OneBookService:
    @staticmethod
    def service(pk):
        book = Book.objects.get(pk=pk)
        if not book:
            return Response({"Book not found!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework import status

from ..models import Author
from ..serializers import AuthorSerializer


class OneAuthorService:
    @staticmethod
    def service(pk=None):
        author = Author.objects.get(pk=pk)
        if not author:
            return Response({"Author not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

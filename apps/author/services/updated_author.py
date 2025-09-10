from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from ..models import Author
from ..serializers import AuthorSerializer


class UpdatedAuthorService:
    @staticmethod
    def service(author_id, author_data):
        try:
            author = Author.objects.get(pk=author_id)
        except ObjectDoesNotExist:
            raise NotFound("Author not found!")

        serializer = AuthorSerializer(author, data=author_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

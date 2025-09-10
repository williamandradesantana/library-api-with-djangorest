from rest_framework.response import Response
from rest_framework import status

from ..models import Author
from ..serializers import AuthorSerializer


class CreateAuthorService:
    @staticmethod
    def service(request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"data": serializer.validated_data}, status=status.HTTP_201_CREATED
        )

from rest_framework.response import Response
from rest_framework import status

from ..serializers import BookSerializer

from apps.author.models import Author


class CreateBookService:
    @staticmethod
    def service(request):
        data = request.data
        author_id = data.get("author")

        if not author_id:
            return Response(
                {"errors": "Author ID is required!"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return Response(
                {"errors": f"Author with id {author_id} does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

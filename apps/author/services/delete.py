from rest_framework.response import Response
from rest_framework import status

from ..models import Author

class DeleteAuthorService:
    @staticmethod
    def service(pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(
                {"data": "Author not found"}, status=status.HTTP_404_NOT_FOUND
            )

        author.is_active = False
        author.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

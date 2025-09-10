from rest_framework.response import Response

from ..models import Author


class ListAllAuthorsService:
    @staticmethod
    def service():
        return Author.objects.filter(is_active=True)

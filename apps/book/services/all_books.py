from rest_framework.response import Response

from ..models import Book


class ListAllBooksService:
    @staticmethod
    def service():
        return Book.objects.filter(is_active=True)

from rest_framework.pagination import PageNumberPagination


class PaginateService:
    @staticmethod
    def paginate(queryset, request, serializer_class, page_size=5):
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

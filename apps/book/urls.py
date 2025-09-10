from django.urls import path

from .views import BookDetailAPIView, BookListAPIView

urlpatterns = [
    path("", BookListAPIView.as_view(), name="book_list"),
    path("<int:pk>/", BookDetailAPIView.as_view(), name="book_detail"),
]

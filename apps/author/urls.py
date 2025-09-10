from django.urls import path

from .views import AuthorListAPIView, AuthorDetailAPIView

urlpatterns = [
    path("", AuthorListAPIView.as_view(), name="author_list"),
    path("<int:pk>/", AuthorDetailAPIView.as_view(), name="author_detail"),
]

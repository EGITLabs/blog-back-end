from django.urls import path
from .views import PostListCreate, PostDetail, CategoryList

urlpatterns = [
    path("posts/", PostListCreate.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("categories/", CategoryList.as_view(), name="category-list"),
]

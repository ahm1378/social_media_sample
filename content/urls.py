from django.urls import path
from content.views import PostListCreateApiView

urlpatterns = [
    path('posts/', PostListCreateApiView.as_view(), name="post"),
]
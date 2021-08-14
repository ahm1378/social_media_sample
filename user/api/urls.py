from django.urls import path
from user.api.views import ProfileApiView
urlpatterns = [
    path('profile/<str:username>/',ProfileApiView.as_view())
    ]
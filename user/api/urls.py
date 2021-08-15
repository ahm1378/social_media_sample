from django.urls import path
from user.api.views import ProfileApiView,ProfileUpdateRe
urlpatterns = [
    path('profile/<str:username>/',ProfileApiView.as_view()),
    path('profile',ProfileUpdateRe.as_view())
    ]
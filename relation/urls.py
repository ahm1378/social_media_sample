from django.urls import path
from relation.views import FollowView, FoLLowersListAPIView

urlpatterns = [
    path('<str:username>/follow', FollowView.as_view(), name="follow_unfollow"),
    path('followers', FoLLowersListAPIView.as_view(), name="followers")
]

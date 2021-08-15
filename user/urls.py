from django.urls import path
from user.views import RegisterView, LoginView, ProfileUpdate, UserDetail

urlpatterns = [
    path('register', RegisterView.as_view(), name="auth_register"),
    path('login', LoginView.as_view(), name="login"),
    path('update', ProfileUpdate.as_view(), name="update"),
    path('<str:username>', UserDetail.as_view(), name="detail")
]


# Create your views here.
from content.serializer import Postserializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from content.models import Post


class PostListCreateApiView(ListCreateAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = Postserializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

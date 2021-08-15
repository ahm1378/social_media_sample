from django.http import Http404
from django.views.generic import View
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from relation.models import Relation
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from relation.serializer import RelationSeriazer
User=get_user_model()


class FollowView(View):

    def get(self):
        try:
            user=User.objects.get(username=self.kwargs['username'])
        except User.DoesNotExists:
            raise Http404
        return user

    def post(self,request,*args,**kwargs):
        user=self.get()
        if user ==request.user:
            return redirect('detail',username=user.username)
        qs=Relation.objects.filter(from_user=request.user,to_user=user)
        if qs.exists():
            qs.delete()
        else:
            Relation.objects.create(from_user=request.user,to_user=user)
        return redirect('detail',username=user.username)


#Rest_frame_work
class FoLLowersListAPIView(ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Relation.objects.all()
    serializer_class = RelationSeriazer

    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(to_user=self.request.user)
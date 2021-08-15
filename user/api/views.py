from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user.api.serialize import UsserSerialize
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
User = get_user_model()


class ProfileApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsserSerialize
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    # def get(self,request,username,*args,**kwargs):
    #     try:
    #         user=User.objects.get(username=username)
    #     except User.DoeeNotExists:
    #         return Response({
    #             'eror':'cant find user',
    #
    #         },status=status.HTTP_404_NOT_FOUND)
    #     serializer=UsserSerialize(instance=user)
        # return Response({
        #     'username':user.username,
        #     'email':user.email,
        #     'phone_number':user.phone_number
        # }
        # )
        # return Response(serializer.data)


class ProfileUpdateRe(RetrieveUpdateAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UsserSerialize

    def get_object(self):
        return self.request.user



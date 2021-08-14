from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from user.api.serialize import UsserSerialize
User=get_user_model()


class ProfileApiView(APIView):

    def get(self,request,username,*args,**kwargs):
        try:
            user=User.objects.get(username=username)
        except User.DoeeNotExists:
            return Response({
                'eror':'cant find user',

            },status=status.HTTP_404_NOT_FOUND)
        serializer=UsserSerialize(instance=user)
        # return Response({
        #     'username':user.username,
        #     'email':user.email,
        #     'phone_number':user.phone_number
        # }
        # )
        return Response(serializer.data)

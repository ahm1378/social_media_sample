from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()


class UsserSerialize(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','email','phone_number','bio','website']
class UsserSerializeLight(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','bio','website']
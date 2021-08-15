from rest_framework import serializers
from content.models import Post, PostMedia
from user.api.serialize import UsserSerializeLight
from location.serializer import LocationSerializer


class PostMediaSerilize(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['file_media', 'type_choice']


class Postserializer(serializers.ModelSerializer):
    user = UsserSerializeLight()
    location = LocationSerializer()
    medias = PostMediaSerilize(many=True)

    class Meta:
        model = Post
        fields = ['title', 'caption', 'user', 'location', 'medias']

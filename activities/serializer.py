from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import ValidationError
from activities.models import Comment
from relation.models import Relation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['caption', 'post', 'reply_to']

    def validate(self, attrs):
        request = self.context['request']
        if attrs['reply_to'] is not None and attrs['reply_to'].post != attrs['post']:
            raise ValidationError(_("post and comment post are not same"))
        qs = Relation.objects.filter(from_user=request.user, to_user=attrs['post'].user).exists()
        if request.user != attrs['post'].user and not qs:
            raise ValidationError(_("You cant add post to this comment"))
        return attrs

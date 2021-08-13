from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
# Create your models here.
User=get_user_model()


class Relation(models.Model):
    from_user=models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return "Like from {} to {}".format(self.from_user,self.to_user)

    def get_from_user_name(self):
        return self.from_user.username

    def get_to_user_name(self):
        return self.to_user.username



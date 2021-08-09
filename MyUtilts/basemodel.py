from django.db import models
from django.utils.translation import ugettext_lazy as _

class BaseModel(models.Model):
    creat_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:

        abstract=True

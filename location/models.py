from django.db import models

# Create your models here.

from MyUtilts.basemodel import BaseModel,_


class Location(BaseModel):
    title=models.CharField(max_length=20)
    points=models.JSONField(_("points"))

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

from django.db import models
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from MyUtilts.basemodel import BaseModel


class Location(BaseModel):
    title = models.CharField(max_length=20)
    points = models.JSONField(_("points"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

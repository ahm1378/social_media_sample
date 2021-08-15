from django.db import models
from MyUtilts.basemodel import BaseModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.contrib.auth import get_user_model

from location.models import Location

user_model = get_user_model()


class Post(BaseModel):
    title = models.CharField(_("title"), max_length=400)
    caption = models.TextField(_("caption"), blank=True)
    user = models.ForeignKey(user_model, related_name="posts", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name="posts", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostMedia(BaseModel):
    IMAGE = 0
    VIDEO = 1
    post = models.ForeignKey(Post, related_name="medias", on_delete=models.CASCADE)
    file_media = models.FileField(_("media file"), upload_to='post/files')
    choices = (
        (IMAGE, _("image")),
        (VIDEO, _("Video"))
    )
    type_choice = models.SmallIntegerField(_("media"), choices=choices)

    def __str__(self):
        return self.post.caption

    class Meta:
        verbose_name = _('PostMedia')
        verbose_name_plural = _('PostMedia')


class Tag(BaseModel):
    title = models.CharField(_("title"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class UserTag(models.Model):
    post = models.ForeignKey(Post, related_name="tagged_users", on_delete=models.CASCADE)
    user = models.ForeignKey(user_model, related_name="tagged_users", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('usertag')
        verbose_name_plural = _('tagged_users')


class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name="posttags", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name="posttags", on_delete=models.CASCADE)

    def __str__(self):
        return self.post.tag

    class Meta:
        verbose_name = _('postag')
        verbose_name_plural = _('posttags')

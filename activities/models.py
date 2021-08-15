from django.db import models
from MyUtilts.basemodel import BaseModel, _
from django.contrib.auth import get_user_model
from content.models import Post
my_user = get_user_model()
# Create your models here.


class Comment(BaseModel):
    Post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(my_user, related_name="comments", on_delete=models.CASCADE)
    caption = models.ForeignKey('self', related_name="comments", on_delete=models.CASCADE)


class LikeComment(BaseModel):
    value = models.BooleanField(_("value"))
    comment = models.ForeignKey(Comment, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(my_user, related_name="likes", on_delete=models.CASCADE)


class LikePost(BaseModel):
    value = models.BooleanField()
    post = models.ForeignKey(Post, related_name="likePosts", on_delete=models.CASCADE)
    user = models.ForeignKey(my_user, related_name="LikePosts", on_delete=models.CASCADE)

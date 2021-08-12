from django.contrib import admin
from activities.models import Comment,LikeComment,LikePost


class CommentAdmin(admin.ModelAdmin):
    list_display = ['Post','user']


admin.site.register(Comment,CommentAdmin)
admin.site.register(LikeComment)
admin.site.register(LikePost)

from django.contrib import admin
from content.models import Post, PostTag,  PostMedia, UserTag


# Register your models here.

class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1


class PostMediaInline(admin.TabularInline):
    model = PostMedia
    extra = 1


class UserTage(admin.TabularInline):
    model = UserTag
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    inlines = [UserTage, PostTagInline, PostMediaInline]


admin.site.register(Post, PostAdmin)

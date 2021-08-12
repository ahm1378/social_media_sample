from django.contrib import admin
from content.models import Post,PostTag,Tag,PostMedia
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['caption','user']

class PostMediaAdmin(admin.ModelAdmin):
    list_display = ['file_media','post']
    list_filter = ['file_media']

admin.site.register(Post,PostAdmin)
admin.site.register(PostTag)
admin.site.register(Tag)
admin.site.register(PostMedia,PostMediaAdmin)

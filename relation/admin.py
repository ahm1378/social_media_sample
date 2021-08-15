from django.contrib import admin
from relation.models import Relation
# Register your models here.


class RelationAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user']


admin.site.register(Relation, RelationAdmin)

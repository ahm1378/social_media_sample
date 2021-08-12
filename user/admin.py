from django.contrib import admin

# Register your models here.
from user.models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


admin.site.register(User, CustomUserAdmin)

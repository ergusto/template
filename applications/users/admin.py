# Register your models here.
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    model = User

# Register your models here.
admin.site.register(User, UserAdmin)

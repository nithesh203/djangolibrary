from django.contrib import admin

# Register your models here.

from users.models import Users,CustomUser
admin.site.register(Users)

admin.site.register(CustomUser)
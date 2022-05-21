from django.contrib import admin

from .models import User, Organization

admin.site.register(Organization)
admin.site.register(User)

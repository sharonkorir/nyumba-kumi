from django.contrib import admin
from .models import Profile, Business, Neighbourhood

# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
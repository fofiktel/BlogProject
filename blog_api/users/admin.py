from django.contrib import admin
from .models import User, Profile, Country, Rang
admin.site.register(User)
# Register your models here.
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Rang)
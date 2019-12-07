from django.contrib import admin

# Register your models here.

from . models import Platform, Game, Developer

admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(Developer)


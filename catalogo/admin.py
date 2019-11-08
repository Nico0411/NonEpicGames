from django.contrib import admin

# Register your models here.

from . models import Platform, Game, GameInstance, Developer

admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(GameInstance)
admin.site.register(Developer)

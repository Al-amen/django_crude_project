from django.contrib import admin

# Register your models here.

from firstapp import models

admin.site.register(models.Musician)

class MusicianAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','instrument',]

admin.site.register(models.Album)
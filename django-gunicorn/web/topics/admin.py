from django.contrib import admin

from .models import Person, Musician, Album

admin.site.register((Person, Musician, Album))
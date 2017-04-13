from django.contrib import admin

from .models import Person, Musician, Album, Car, Manufacturer, Restaurant

admin.site.register((Person, Musician, Album, Car, Manufacturer, Restaurant))
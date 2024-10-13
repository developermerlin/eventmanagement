from django.contrib import admin
from .models import Event, Venue, Dish, Entertainment
# Register your models here.
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Dish)
admin.site.register(Entertainment)
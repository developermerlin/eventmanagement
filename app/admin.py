from django.contrib import admin
from .models import Event, Venue, Dish, Entertainment,Booking_Venue,Book_Event,Afrimoney,Creditcard
# Register your models here.
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Dish)
admin.site.register(Entertainment)
admin.site.register(Booking_Venue)
admin.site.register(Book_Event)
admin.site.register(Afrimoney)
admin.site.register(Creditcard)
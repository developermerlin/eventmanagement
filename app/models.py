from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.event_name
    

class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    venue_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)   
    facilities = models.TextField()  
    address = models.CharField(max_length=100)
    contact = models.IntegerField() 
    profile = models.ImageField(upload_to='venue/', blank=True, null=True) 
    video = models.FileField(upload_to='venue/', blank=True, null=True)  
    def __str__(self):
        return self.venue_name
    
    
class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_venue = models.CharField(max_length=100)
    cost_of_dish = models.DecimalField(max_digits=10, decimal_places=2) 
    def __str__(self):
        return self.dish_name


class Entertainment(models.Model):
    entertainment_name = models.CharField(max_length=100)
    entertainment_venue = models.CharField(max_length=100)
    entertainment_cost= models.DecimalField(max_digits=10, decimal_places=2) 
    def __str__(self):
        return self.entertainment_name
    
    
class Photography(models.Model):
    photography_name = models.CharField(max_length=100)
    photography_venue = models.CharField(max_length=100)
    photography_cost= models.DecimalField(max_digits=10, decimal_places=2) 
    def __str__(self):
        return self.photography_name
    
    
class Drinks(models.Model):
    drinks_name = models.CharField(max_length=100)
    drinks_venue = models.CharField(max_length=100)
    drinks_cost= models.DecimalField(max_digits=10, decimal_places=2) 
    def __str__(self):
        return self.drinks_name
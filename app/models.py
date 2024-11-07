from datetime import timezone
from django.db import models
from django.utils import timezone  


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.event_name
    

class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.IntegerField() 
    capacity = models.IntegerField() 
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
    

class Booking_Venue(models.Model):
    venue_name = models.ForeignKey(Venue, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    dish1 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='venue_dish1', null=True, blank=True)
    dish2 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='venue_dish2', null=True, blank=True)
    dish3 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='venue_dish3', null=True, blank=True)
    entertainment1 = models.ForeignKey(Entertainment, on_delete=models.CASCADE, related_name='venue_entertainment1', null=True, blank=True)
    entertainment2 = models.ForeignKey(Entertainment, on_delete=models.CASCADE, related_name='venue_entertainment2', null=True, blank=True)
    entertainment3 = models.ForeignKey(Entertainment, on_delete=models.CASCADE, related_name='venue_entertainment3', null=True, blank=True)
    photography = models.ForeignKey(Photography,on_delete=models.CASCADE , null=True, blank=True)
    drinks1 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks1', null=True, blank=True)
    drinks2 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks2', null=True, blank=True)
    drinks3 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks3', null=True, blank=True)
    drinks4 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks4', null=True, blank=True)
    
    def __str__(self):
        return str(self.venue_name)



class Book_Event(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('successful', 'Successful'),
    ]
    venue_name = models.ForeignKey(Booking_Venue, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    customer_contact = models.IntegerField()
    number_of_guests = models.IntegerField(null=True, blank=True) 
    dish1 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='venue_dish11', null=True, blank=True)
    dish2 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='venue_dish21', null=True, blank=True)
    dish3 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='venue_dish31', null=True, blank=True)
    entertainment1 = models.ForeignKey(Entertainment, on_delete=models.CASCADE, related_name='venue_entertainment11', null=True, blank=True)
    entertainment2 = models.ForeignKey(Entertainment, on_delete=models.CASCADE, related_name='venue_entertainment21', null=True, blank=True)
    entertainment3 = models.ForeignKey(Entertainment, on_delete=models.CASCADE, related_name='venue_entertainment31', null=True, blank=True)
    photography = models.ForeignKey(Photography, on_delete=models.CASCADE, null=True, blank=True)
    drinks1 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks11', null=True, blank=True)
    drinks2 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks21', null=True, blank=True)
    drinks3 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks31', null=True, blank=True)
    drinks4 = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='venue_drinks41', null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # New field added

    
    def calculate_grand_total(self):
        total_cost = 0

        # Calculate venue cost
        total_cost += self.venue_name.cost_per_day

        # Calculate total cost of dishes multiplied by number of guests
        total_dishes_cost = 0
        for dish in [self.dish1, self.dish2, self.dish3]:
            if dish:
                total_dishes_cost += dish.cost_of_dish
        
        total_cost += total_dishes_cost * self.number_of_guests  # Total cost of dishes for all guests

        # Calculate total cost of drinks multiplied by number of guests
        total_drinks_cost = 0
        for drink in [self.drinks1, self.drinks2, self.drinks3, self.drinks4]:
            if drink:
                total_drinks_cost += drink.drinks_cost
        
        total_cost += total_drinks_cost * self.number_of_guests  # Total cost of drinks for all guests

        # Calculate cost of entertainment
        total_entertainment_cost = 0
        for entertainment in [self.entertainment1, self.entertainment2, self.entertainment3]:
            if entertainment:
                total_entertainment_cost += entertainment.entertainment_cost
        
        total_cost += total_entertainment_cost  # Adding entertainment cost to total

        # Calculate cost of photography
        if self.photography:
            total_cost += self.photography.photography_cost  # Adding photography cost to total

        return total_cost

    def __str__(self):
        return str(self.venue_name)
    


class Afrimoney(models.Model):
    user_name = models.CharField(max_length=50, null=True)
    phone_number = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pin = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return str(self.phone_number)
    

class Creditcard(models.Model):
    card_number = models.IntegerField(null=True)
    name_on_card= models.CharField(max_length=50, null=True)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True) 
    cvv = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return str(self.name_on_card)
    


from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Event, Venue, Dish, Entertainment, Photography,Drinks
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def users(request):
    return render(request, 'users.html')



# ADD EVENT
def event(request):
    events = Event.objects.all()
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')

        event = Event(
            event_name=event_name,
            event_description=event_description
        )

        event.save()
        messages.success(request, "Event added Successfully")
        return redirect('event')
    return render(request, 'event.html',{'events':events})

def edit_event(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')

        event.event_name = event_name
        event.event_description = event_description

        event.save()
        messages.success(request, "Category updated successfully!")
        return redirect('event')
    return render(request, 'edit_event.html', {'event': event})

# Delete Category
def delete_event(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect('event')
    return render(request, 'delete_event.html', {'event': event})


# VENUE 
def venue(request):
    if request.method == 'POST':
        venue_name = request.POST.get('venue_name')
        event_id = request.POST.get('event')
        cost_per_day = request.POST.get('cost_per_day')
        facilities = request.POST.get('facilities')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        profile = request.FILES.get('file')
        video = request.FILES.get('video')
        venue_event = Event.objects.get(id=event_id)
        

        venue = Venue(
            venue_name=venue_name,
            venue_event=venue_event,
            cost_per_day=cost_per_day,
            facilities=facilities,
            address=address,
            contact=contact,
            video=video,
            profile=profile
            )
        venue.save()
        messages.success(request, "Venue added successfully!")
        return redirect('venue')
    events = Event.objects.all()
    venues = Venue.objects.all()
    return render(request, 'venue.html', {'events': events,'venues':venues})


def edit_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    if request.method == 'POST':
        venue_name = request.POST.get('venue_name')
        event_id = request.POST.get('event')
        cost_per_day = request.POST.get('cost_per_day')
        facilities = request.POST.get('facilities')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        profile = request.FILES.get('file') if 'file' in request.FILES else venue.profile
        video = request.FILES.get('video') if 'video' in request.FILES else venue.video


        venue_event = Event.objects.get(id=event_id)
        venue.venue_name = venue_name
        venue.venue_event = venue_event
        venue.cost_per_day = cost_per_day
        venue.facilities = facilities
        venue.address = address 
        venue.contact = contact 
        venue.profile = profile
        venue.video = video
        venue.save()

        messages.success(request, "Venue updated successfully!")
        return redirect('venue')
    events = Event.objects.all()
    return render(request, 'edit_venue.html', {'venue': venue, 'events': events})


def delete_venue(request, venue_id):
    if request.method == 'POST':
        venue = Venue.objects.get(id=venue_id)
        venue.delete()
        messages.success(request, "Venue deleted successfully!")
        return redirect('venue')
    return render(request, 'delete_venue.html')


def view_venue(request, venue_id):
    # Get the product using its ID or return a 404 error if not found
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'view_venue.html', {
        'venue': venue,
    })
    
    
    # dish



def dish(request):
    dishes = Dish.objects.all()
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        dish_venue = request.POST.get('dish_venue')
        cost_of_dish = request.POST.get('cost_of_dish')
        
        
        dish = Dish(
            dish_name=dish_name,
            dish_venue=dish_venue,
            cost_of_dish = cost_of_dish
            
        )

        dish.save()
        messages.success(request, "Dish added Successfully")
        return redirect('dish')
    return render(request, 'dish.html',{'dishes':dishes})
    
def edit_dish(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        dish_venue = request.POST.get('dish_venue')
        cost_of_dish = request.POST.get('cost_of_dish')

        dish.dish_name = dish_name
        dish.dish_venue = dish_venue
        dish.cost_of_dish = cost_of_dish

        dish.save()
        messages.success(request, "Dish updated successfully!")
        return redirect('dish')
    return render(request, 'edit_dish.html', {'dish': dish})

# Delete Category
def delete_dish(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == 'POST':
        dish.delete()
        messages.success(request, "Dish Deleted successfully!")
        return redirect('dish')
    return render(request, 'delete_dish.html', {'dish': dish})


# Entertainment
def entertainment(request):
    entertainments = Entertainment.objects.all()
    if request.method == 'POST':
        entertainment_name = request.POST.get('entertainment_name')
        entertainment_venue = request.POST.get('entertainment_venue')
        entertainment_cost = request.POST.get('entertainment_cost')

        entertainment = Entertainment(
            entertainment_name=entertainment_name,
            entertainment_venue=entertainment_venue,
            entertainment_cost=entertainment_cost,
            
        )

        entertainment.save()
        messages.success(request, "Entertainment added Successfully")
        return redirect('entertainment')
    return render(request, 'entertainment.html',{'entertainments':entertainments})


def edit_entertainment(request, pk):
    entertainment = Entertainment.objects.get(pk=pk)
    if request.method == 'POST':
        entertainment_name = request.POST.get('entertainment_name')
        entertainment_venue = request.POST.get('entertainment_venue')
        entertainment_cost = request.POST.get('entertainment_cost')

        entertainment.entertainment_name = entertainment_name
        entertainment.entertainment_venue = entertainment_venue
        entertainment.entertainment_cost = entertainment_cost
       
        entertainment.save()
        messages.success(request, "Entertainment updated successfully!")
        return redirect('entertainment')
    return render(request, 'edit_entertainment.html', {'entertainment': entertainment})


def delete_entertainment(request, pk):
    entertainment = Entertainment.objects.get(pk=pk)
    if request.method == 'POST':
        entertainment.delete()
        messages.success(request, "Entertainment deleted successfully!")
        return redirect('entertainment')
    return render(request, 'delete_entertainment.html', {'entertainment': entertainment})




def photography(request):
    photographys = Photography.objects.all()
    if request.method == 'POST':
        photography_name = request.POST.get('photography_name')
        photography_venue = request.POST.get('photography_venue')
        photography_cost = request.POST.get('photography_cost')

        photography = Photography(
            photography_name=photography_name,
            photography_venue=photography_venue,
            photography_cost=photography_cost,
            
        )

        photography.save()
        messages.success(request, "Photography added Successfully")
        return redirect('photography')
    return render(request, 'photography.html',{'photographys':photographys})


def edit_photography(request, pk):
    photography = Photography.objects.get(pk=pk)
    if request.method == 'POST':
        photography_name = request.POST.get('photography_name')
        photography_venue = request.POST.get('photography_venue')
        photography_cost = request.POST.get('photography_cost')

        photography.photography_name = photography_name
        photography.photography_venue = photography_venue
        photography.photography_cost = photography_cost
       
        photography.save()
        messages.success(request, "Photography updated successfully!")
        return redirect('photography')
    return render(request, 'edit_photography.html', {'photography': photography})


def delete_photography(request, pk):
    photography = Photography.objects.get(pk=pk)
    if request.method == 'POST':
        photography.delete()
        messages.success(request, "Photography deleted successfully!")
        return redirect('photography')
    return render(request, 'delete_photography.html', {'photography': photography})




def drinks(request):
    drinks = Drinks.objects.all()
    if request.method == 'POST':
        drink_name = request.POST.get('drink_name')
        drink_venue = request.POST.get('drink_venue')
        drink_cost = request.POST.get('drink_cost')
        
        drink = Drinks(
            drinks_name=drink_name,
            drinks_venue=drink_venue,
            drinks_cost = drink_cost
        )

        drink.save()
        messages.success(request, "Drink added Successfully")
        return redirect('drinks')
    return render(request, 'drinks.html',{'drinks':drinks})


def edit_drinks(request, pk):
    drink = Drinks.objects.get(pk=pk)
    if request.method == 'POST':
        drink_name = request.POST.get('drink_name')
        drink_venue = request.POST.get('drink_venue')
        drink_cost = request.POST.get('drink_cost')
        

        drink.drinks_name = drink_name
        drink.drinks_venue = drink_venue
        drink.drinks_cost = drink_cost
        

        drink.save()
        messages.success(request, "Drink updated successfully!")
        return redirect('drinks')
    return render(request, 'edit_drinks.html', {'drink': drink})

# Delete Category
def delete_drinks(request, pk):
    drink = Drinks.objects.get(pk=pk)
    if request.method == 'POST':
        drink.delete()
        messages.success(request, "Drinks Deleted successfully!")
        return redirect('drinks')
    return render(request, 'delete_drinks.html', {'drink': drink})

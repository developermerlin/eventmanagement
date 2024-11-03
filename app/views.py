from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Booking_Venue, Venue, Event, Dish, Entertainment, Photography, Drinks
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
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        profile = request.FILES.get('file')
        video = request.FILES.get('video')
        

        venue = Venue(
            venue_name=venue_name,
            address=address,
            contact=contact,
            video=video,
            profile=profile
            )
        venue.save()
        messages.success(request, "Venue added successfully!")
        return redirect('venue')
    venues = Venue.objects.all()
    return render(request, 'venue.html', {'venues':venues})


def edit_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    if request.method == 'POST':
        venue_name = request.POST.get('venue_name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        profile = request.FILES.get('file') if 'file' in request.FILES else venue.profile
        video = request.FILES.get('video') if 'video' in request.FILES else venue.video


        venue.venue_name = venue_name
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








def booking_venue(request):
    if request.method == 'POST':
        # Retrieving form data
        venue_name_id = request.POST.get('venue_name')
        event_id = request.POST.get('event')
        cost_per_day = request.POST.get('cost_per_day')
        dish1_id = request.POST.get('dish1')
        dish2_id = request.POST.get('dish2')
        dish3_id = request.POST.get('dish3')
        entertainment1_id = request.POST.get('entertainment1')
        entertainment2_id = request.POST.get('entertainment2')
        entertainment3_id = request.POST.get('entertainment3')
        photography_id = request.POST.get('photography')
        drinks1_id = request.POST.get('drinks1')
        drinks2_id = request.POST.get('drinks2')
        drinks3_id = request.POST.get('drinks3')
        drinks4_id = request.POST.get('drinks4')

        # Creating the Booking_Venue instance
        Booking_Venue.objects.create(
            venue_name_id=venue_name_id,
            event_id=event_id,
            cost_per_day=cost_per_day,
            dish1_id=dish1_id,
            dish2_id=dish2_id,
            dish3_id=dish3_id,
            entertainment1_id=entertainment1_id,
            entertainment2_id=entertainment2_id,
            entertainment3_id=entertainment3_id,
            photography_id=photography_id,
            drinks1_id=drinks1_id,
            drinks2_id=drinks2_id,
            drinks3_id=drinks3_id,
            drinks4_id=drinks4_id,
        )

        # Adding a success message
        messages.success(request, "Booking Venue has been successfully created!")

        return redirect('booking_venue')  # Redirect after successful creation
    
    # Querying related models for dropdown values
    venues = Venue.objects.all()
    events = Event.objects.all()
    dishes = Dish.objects.all()
    entertainments = Entertainment.objects.all()
    photographies = Photography.objects.all()
    drinks = Drinks.objects.all()
    booking_venues = Booking_Venue.objects.all()

    # Passing querysets to template
    context = {
        'venues': venues,
        'events': events,
        'dishes': dishes,
        'entertainments': entertainments,
        'photographies': photographies,
        'drinks': drinks,
        'booking_venues':booking_venues,
    }
    return render(request, 'booking_venue.html', context)



def edit_booking_venue(request, booking_venue_id):
    booking_venue = get_object_or_404(Booking_Venue, id=booking_venue_id)

    if request.method == 'POST':
        # Retrieving form data
        venue_name_id = request.POST.get('venue_name')
        event_id = request.POST.get('event')
        cost_per_day = request.POST.get('cost_per_day')
        dish1_id = request.POST.get('dish1')
        dish2_id = request.POST.get('dish2')
        dish3_id = request.POST.get('dish3')
        entertainment1_id = request.POST.get('entertainment1')
        entertainment2_id = request.POST.get('entertainment2')
        entertainment3_id = request.POST.get('entertainment3')
        photography_id = request.POST.get('photography')
        drinks1_id = request.POST.get('drinks1')
        drinks2_id = request.POST.get('drinks2')
        drinks3_id = request.POST.get('drinks3')
        drinks4_id = request.POST.get('drinks4')

        # Updating the Booking_Venue instance
        booking_venue.venue_name_id = venue_name_id
        booking_venue.event_id = event_id
        booking_venue.cost_per_day = cost_per_day
        booking_venue.dish1_id = dish1_id
        booking_venue.dish2_id = dish2_id
        booking_venue.dish3_id = dish3_id
        booking_venue.entertainment1_id = entertainment1_id
        booking_venue.entertainment2_id = entertainment2_id
        booking_venue.entertainment3_id = entertainment3_id
        booking_venue.photography_id = photography_id
        booking_venue.drinks1_id = drinks1_id
        booking_venue.drinks2_id = drinks2_id
        booking_venue.drinks3_id = drinks3_id
        booking_venue.drinks4_id = drinks4_id
        booking_venue.save()

        # Adding a success message
        messages.success(request, "Booking Venue has been successfully updated!")

        return redirect('booking_venue')  # Redirect after successful update

    # Querying related models for dropdown values
    venues = Venue.objects.all()
    events = Event.objects.all()
    dishes = Dish.objects.all()
    entertainments = Entertainment.objects.all()
    photographies = Photography.objects.all()
    drinks = Drinks.objects.all()

    # Passing querysets to template
    context = {
        'venues': venues,
        'events': events,
        'dishes': dishes,
        'entertainments': entertainments,
        'photographies': photographies,
        'drinks': drinks,
        'booking_venue': booking_venue,
    }
    return render(request, 'edit_booking_venue.html', context)



def delete_booking_venue(request, booking_venue_id):
    booking_venue = get_object_or_404(Booking_Venue, id=booking_venue_id)

    if request.method == 'POST':
        booking_venue.delete()
        messages.success(request, "Booking Venue has been successfully deleted!")
        return redirect('booking_venue')  # Redirect after successful deletion

    return render(request, 'delete_booking_venue.html', {'booking_venue': booking_venue})



def available_venue(request):
    if request.method == 'POST':
        # Retrieving form data
        venue_name_id = request.POST.get('venue_name')
        event_id = request.POST.get('event')
        cost_per_day = request.POST.get('cost_per_day')
        dish1_id = request.POST.get('dish1')
        dish2_id = request.POST.get('dish2')
        dish3_id = request.POST.get('dish3')
        entertainment1_id = request.POST.get('entertainment1')
        entertainment2_id = request.POST.get('entertainment2')
        entertainment3_id = request.POST.get('entertainment3')
        photography_id = request.POST.get('photography')
        drinks1_id = request.POST.get('drinks1')
        drinks2_id = request.POST.get('drinks2')
        drinks3_id = request.POST.get('drinks3')
        drinks4_id = request.POST.get('drinks4')

        # Creating the Booking_Venue instance
        Booking_Venue.objects.create(
            venue_name_id=venue_name_id,
            event_id=event_id,
            cost_per_day=cost_per_day,
            dish1_id=dish1_id,
            dish2_id=dish2_id,
            dish3_id=dish3_id,
            entertainment1_id=entertainment1_id,
            entertainment2_id=entertainment2_id,
            entertainment3_id=entertainment3_id,
            photography_id=photography_id,
            drinks1_id=drinks1_id,
            drinks2_id=drinks2_id,
            drinks3_id=drinks3_id,
            drinks4_id=drinks4_id,
        )

        # Adding a success message
        messages.success(request, "Booking Venue has been successfully created!")

        return redirect('available_venue')  # Redirect after successful creation
    
    # Querying related models for dropdown values
    venues = Venue.objects.all()
    events = Event.objects.all()
    dishes = Dish.objects.all()
    entertainments = Entertainment.objects.all()
    photographies = Photography.objects.all()
    drinks = Drinks.objects.all()
    booking_venues = Booking_Venue.objects.all()

    # Passing querysets to template
    context = {
        'venues': venues,
        'events': events,
        'dishes': dishes,
        'entertainments': entertainments,
        'photographies': photographies,
        'drinks': drinks,
        'booking_venues':booking_venues,
    }
    return render(request, 'available_venue.html', context)

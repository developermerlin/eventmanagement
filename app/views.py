from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Booking_Venue, Venue, Event, Dish, Entertainment, Photography, Drinks,Book_Event,Afrimoney,Creditcard
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    available_venue = Booking_Venue.objects.all().count()
    books = Book_Event.objects.all().count()
    events = Event.objects.all().count()
    mobile = Afrimoney.objects.all().count()
    card = Creditcard.objects.all().count()
    food = Dish.objects.all().count()
    drinks = Drinks.objects.all().count()
    users = User.objects.all().count()
    
    context = {
        'available_venue':available_venue,
        'books':books,
        'events':events,
        'mobile':mobile,
        'food':food,
        'drinks':drinks,
        'users':users,
        'card':card,
        # 'card':card,
    }
    return render(request, 'dashboard.html' ,context)

def users(request):
    available_venue = Booking_Venue.objects.all().count()
    books = Book_Event.objects.all().count()
    
    context = {
        'available_venue':available_venue,
        'books':books
    }
    return render(request, 'users.html',context)



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
        capacity = request.POST.get('capacity')
        profile = request.FILES.get('file')
        video = request.FILES.get('video')
        

        venue = Venue(
            venue_name=venue_name,
            address=address,
            contact=contact,
            capacity=capacity,
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
        capacity = request.POST.get('capacity')
        profile = request.FILES.get('file') if 'file' in request.FILES else venue.profile
        video = request.FILES.get('video') if 'video' in request.FILES else venue.video


        venue.venue_name = venue_name
        venue.address = address 
        venue.contact = contact 
        venue.capacity = capacity 
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



def available_venue_details(request, pk):
    # Retrieve the specific Booking_Venue instance by primary key (ID)
    booking_venue = get_object_or_404(Booking_Venue, pk=pk)
    
    # Pass the instance to the template context
    context = {
        'booking_venue': booking_venue,
    }
    return render(request, 'available_venue_details.html', context)

def booking_history(request):
    book_events = Book_Event.objects.all()  # Retrieve all bookings
    context = {
        'book_events': book_events,
    }
    return render(request, 'booking_history.html', context)




def book_event(request):
    if request.method == 'POST':
        venue_name_id = request.POST.get('venue_name')
        customer = request.POST.get('customer')
        customer_contact = request.POST.get('customer_contact')
        event_id = request.POST.get('event')
        date = request.POST.get('date')
        number_of_guests = int(request.POST.get('number_of_guests'))

        # Fetch selected item IDs, setting them to None if not provided
        dish1_id = request.POST.get('dish1') or None
        dish2_id = request.POST.get('dish2') or None
        dish3_id = request.POST.get('dish3') or None
        entertainment1_id = request.POST.get('entertainment1') or None
        entertainment2_id = request.POST.get('entertainment2') or None
        entertainment3_id = request.POST.get('entertainment3') or None
        photography_id = request.POST.get('photography') or None
        drinks1_id = request.POST.get('drinks1') or None
        drinks2_id = request.POST.get('drinks2') or None
        drinks3_id = request.POST.get('drinks3') or None
        drinks4_id = request.POST.get('drinks4') or None

        # Initialize costs
        total_dishes_cost = 0
        total_drinks_cost = 0
        total_entertainment_cost = 0
        total_photography_cost = 0

        # Calculating total cost for dishes
        for dish_id in [dish1_id, dish2_id, dish3_id]:
            if dish_id:
                dish_cost = Dish.objects.get(id=dish_id).cost_of_dish
                total_dishes_cost += dish_cost * number_of_guests

        # Calculating total cost for drinks
        for drink_id in [drinks1_id, drinks2_id, drinks3_id, drinks4_id]:
            if drink_id:
                drink_cost = Drinks.objects.get(id=drink_id).drinks_cost
                total_drinks_cost += drink_cost * number_of_guests

        # Calculating total cost for entertainment
        for entertainment_id in [entertainment1_id, entertainment2_id, entertainment3_id]:
            if entertainment_id:
                entertainment_cost = Entertainment.objects.get(id=entertainment_id).entertainment_cost
                total_entertainment_cost += entertainment_cost

        # Calculating total cost for photography
        if photography_id:
            total_photography_cost = Photography.objects.get(id=photography_id).photography_cost

        # Calculate venue cost
        booking_venue = Booking_Venue.objects.get(id=venue_name_id)
        venue_cost = booking_venue.cost_per_day

        # Calculate grand total using the defined logic
        grand_total = (
            total_dishes_cost + 
            total_drinks_cost + 
            total_entertainment_cost + 
            total_photography_cost + 
            venue_cost
        )

        # Create the Book_Event instance with status set to 'pending'
        book_event = Book_Event.objects.create(
            venue_name_id=venue_name_id,
            customer=customer,
            customer_contact=customer_contact,
            number_of_guests=number_of_guests,
            date=date,
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
            status='pending',  
        )

        # Add a success message
        messages.success(request, f"Booking Venue has been successfully created! Grand Total: {grand_total:.2f}")

        return redirect('booking_history')  # Redirect after successful creation

    # Query related models for dropdown values
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
    }
    return render(request, 'book_event.html', context)


def booking_history_details(request, pk):
    # Retrieve the specific Book_Event instance by primary key (ID)
    booking_history = get_object_or_404(Book_Event, pk=pk)

    # Calculate the total costs based on selected items in Book_Event
    number_of_guests = booking_history.number_of_guests
    total_dishes_cost = sum(
        (dish.cost_of_dish * number_of_guests) for dish in [
            booking_history.dish1, 
            booking_history.dish2, 
            booking_history.dish3
        ] if dish
    )
    
    total_drinks_cost = sum(
        (drink.drinks_cost * number_of_guests) for drink in [
            booking_history.drinks1, 
            booking_history.drinks2, 
            booking_history.drinks3, 
            booking_history.drinks4
        ] if drink
    )

    total_entertainment_cost = sum(
        entertainment.entertainment_cost for entertainment in [
            booking_history.entertainment1, 
            booking_history.entertainment2, 
            booking_history.entertainment3
        ] if entertainment
    )
    
    total_photography_cost = booking_history.photography.photography_cost if booking_history.photography else 0
    venue_cost = booking_history.venue_name.cost_per_day  # Cost per day from Booking_Venue

    # Calculate grand total
    grand_total = (
        total_dishes_cost +
        total_drinks_cost +
        total_entertainment_cost +
        total_photography_cost +
        venue_cost
    )

    # Pass the data to the template
    context = {
        'booking_history': booking_history,
        'grand_total': grand_total,
    }
    return render(request, 'booking_history_details.html', context)



# ==============================ADMIN BOOKING HISTORY===========================
def admin_booking_history(request):
    book_events = Book_Event.objects.all()  # Retrieve all bookings
    context = {
        'book_events': book_events,
    }
    return render(request, 'admin_booking_history.html', context)




def admin_booking_history_details(request, pk):
    # Retrieve the specific Book_Event instance by primary key (ID)
    booking_history = get_object_or_404(Book_Event, pk=pk)

    # Calculate the total costs based on selected items in Book_Event
    number_of_guests = booking_history.number_of_guests
    total_dishes_cost = sum(
        (dish.cost_of_dish * number_of_guests) for dish in [
            booking_history.dish1, 
            booking_history.dish2, 
            booking_history.dish3
        ] if dish
    )
    
    total_drinks_cost = sum(
        (drink.drinks_cost * number_of_guests) for drink in [
            booking_history.drinks1, 
            booking_history.drinks2, 
            booking_history.drinks3, 
            booking_history.drinks4
        ] if drink
    )

    total_entertainment_cost = sum(
        entertainment.entertainment_cost for entertainment in [
            booking_history.entertainment1, 
            booking_history.entertainment2, 
            booking_history.entertainment3
        ] if entertainment
    )
    
    total_photography_cost = booking_history.photography.photography_cost if booking_history.photography else 0
    venue_cost = booking_history.venue_name.cost_per_day  # Cost per day from Booking_Venue

    # Calculate grand total
    grand_total = (
        total_dishes_cost +
        total_drinks_cost +
        total_entertainment_cost +
        total_photography_cost +
        venue_cost
    )

    # Pass the data to the template
    context = {
        'booking_history': booking_history,
        'grand_total': grand_total,
    }
    return render(request, 'admin_booking_history_details.html', context)


def edit_payment_status(request, booking_id):
    # Fetch the booking using the booking ID
    booking = get_object_or_404(Book_Event, id=booking_id)

    if request.method == 'POST':
        # Get the new status from the form
        new_status = request.POST.get('status')

        # Update the status of the booking
        booking.status = new_status
        booking.save()

        # Add a success message
        messages.success(request, "Booking Payment status has been updated!")

        return redirect('admin_booking_history')  # Redirect to booking history or another page

    # Pass the current status to the template
    context = {
        'booking': booking,
    }
    return render(request, 'edit_payment_status.html', context)

def receipt(request):
    return render(request, 'print_receipt.html')

def print_receipt(request, booking_id):
    # Fetch the booking using the booking ID
    booking = get_object_or_404(Book_Event, id=booking_id)

    number_of_guests = booking.number_of_guests
    total_dishes_cost = sum(
        (dish.cost_of_dish * number_of_guests) for dish in [
            booking.dish1, 
            booking.dish2, 
            booking.dish3
        ] if dish
    )
    
    total_drinks_cost = sum(
        (drink.drinks_cost * number_of_guests) for drink in [
            booking.drinks1, 
            booking.drinks2, 
            booking.drinks3, 
            booking.drinks4
        ] if drink
    )

    total_entertainment_cost = sum(
        entertainment.entertainment_cost for entertainment in [
            booking.entertainment1, 
            booking.entertainment2, 
            booking.entertainment3
        ] if entertainment
    )
    
    total_photography_cost = booking.photography.photography_cost if booking.photography else 0
    venue_cost = booking.venue_name.cost_per_day  # Cost per day from Booking_Venue

    # Calculate grand total
    grand_total = (
        total_dishes_cost +
        total_drinks_cost +
        total_entertainment_cost +
        total_photography_cost +
        venue_cost
    )
    
    # Render the receipt template with booking details
    return render(request, 'print_receipt.html', {'booking': booking, 'grand_total':grand_total})


def booking_payment(request):
    return render(request, 'booking_payment.html')


def booking_payment_page(request):
    bookings = Book_Event.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        pin = request.POST.get('pin')

        afrimoney = Afrimoney(
            user_name=user_name,
            phone_number=phone_number,
            amount=amount,
            pin=pin
        )

        afrimoney.save()
        messages.success(request, "Payment Successfully done. Please wait for some minutes while your booking is being processed")
        return redirect('booking_history')


    # Calculate the grand total for each booking and store it in the booking instance
    for booking in bookings:
        # Get the number of guests
        number_of_guests = booking.number_of_guests

        # Calculate the costs for dishes
        total_dishes_cost = 0
        for dish in [booking.dish1, booking.dish2, booking.dish3]:
            if dish:
                total_dishes_cost += dish.cost_of_dish * number_of_guests

        # Calculate the costs for drinks
        total_drinks_cost = 0
        for drink in [booking.drinks1, booking.drinks2, booking.drinks3, booking.drinks4]:
            if drink:
                total_drinks_cost += drink.drinks_cost * number_of_guests

        # Calculate the costs for entertainment
        total_entertainment_cost = 0
        for entertainment in [booking.entertainment1, booking.entertainment2, booking.entertainment3]:
            if entertainment:
                total_entertainment_cost += entertainment.entertainment_cost

        # Calculate the cost for photography
        total_photography_cost = 0
        if booking.photography:
            total_photography_cost = booking.photography.photography_cost

        # Venue cost (assuming it's a fixed cost per booking)
        venue_cost = booking.venue_name.cost_per_day

        # Calculate the grand total
        booking.grand_total = (
            total_dishes_cost +
            total_drinks_cost +
            total_entertainment_cost +
            total_photography_cost +
            venue_cost
        )

    # Pass the bookings with calculated grand_total to the template
    return render(request, 'booking_payment_page.html', {'booking': bookings})


def booking_payment_process(request, booking_id):
    bookings = get_object_or_404(Book_Event, id=booking_id)
    return render(request, 'booking_payment_page.html', {'bookings': bookings})


def admin_booking_payment_page(request):
    bookings = Book_Event.objects.all()
    afrimoneys = Afrimoney.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        pin = request.POST.get('pin')

        afrimoney = Afrimoney(
            user_name=user_name,
            phone_number=phone_number,
            amount=amount,
            pin=pin
        )

        afrimoney.save()
        messages.success(request, "Payment Successfully done. Please wait for some minutes while your booking is being processed")
        return redirect('booking_history')


    # Calculate the grand total for each booking and store it in the booking instance
    for booking in bookings:
        # Get the number of guests
        number_of_guests = booking.number_of_guests

        # Calculate the costs for dishes
        total_dishes_cost = 0
        for dish in [booking.dish1, booking.dish2, booking.dish3]:
            if dish:
                total_dishes_cost += dish.cost_of_dish * number_of_guests

        # Calculate the costs for drinks
        total_drinks_cost = 0
        for drink in [booking.drinks1, booking.drinks2, booking.drinks3, booking.drinks4]:
            if drink:
                total_drinks_cost += drink.drinks_cost * number_of_guests

        # Calculate the costs for entertainment
        total_entertainment_cost = 0
        for entertainment in [booking.entertainment1, booking.entertainment2, booking.entertainment3]:
            if entertainment:
                total_entertainment_cost += entertainment.entertainment_cost

        # Calculate the cost for photography
        total_photography_cost = 0
        if booking.photography:
            total_photography_cost = booking.photography.photography_cost

        # Venue cost (assuming it's a fixed cost per booking)
        venue_cost = booking.venue_name.cost_per_day

        # Calculate the grand total
        booking.grand_total = (
            total_dishes_cost +
            total_drinks_cost +
            total_entertainment_cost +
            total_photography_cost +
            venue_cost
        )

    return render(request, 'admin_booking_payment_page.html', {'booking': bookings, 'afrimoneys':afrimoneys})


def admin_afrimoney_detail(request, pk):
    payment = get_object_or_404(Afrimoney, pk=pk)
    return render(request, 'admin_afrimoney_detail.html', {'payment': payment})


def booking_payment_page2(request):
    bookings = Book_Event.objects.all()
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        name_on_card = request.POST.get('name_on_card')
        month = request.POST.get('month')
        year = request.POST.get('year')
        cvv = request.POST.get('cvv')

        creditcard = Creditcard(
            card_number=card_number,
            name_on_card=name_on_card,
            month=month,
            year=year,
            cvv=cvv,
        )

        creditcard.save()
        messages.success(request, "Payment Successfully done. Please wait for some minutes while your booking is being processed")
        return redirect('booking_history')


    # Calculate the grand total for each booking and store it in the booking instance
    for booking in bookings:
        # Get the number of guests
        number_of_guests = booking.number_of_guests

        # Calculate the costs for dishes
        total_dishes_cost = 0
        for dish in [booking.dish1, booking.dish2, booking.dish3]:
            if dish:
                total_dishes_cost += dish.cost_of_dish * number_of_guests

        # Calculate the costs for drinks
        total_drinks_cost = 0
        for drink in [booking.drinks1, booking.drinks2, booking.drinks3, booking.drinks4]:
            if drink:
                total_drinks_cost += drink.drinks_cost * number_of_guests

        # Calculate the costs for entertainment
        total_entertainment_cost = 0
        for entertainment in [booking.entertainment1, booking.entertainment2, booking.entertainment3]:
            if entertainment:
                total_entertainment_cost += entertainment.entertainment_cost

        # Calculate the cost for photography
        total_photography_cost = 0
        if booking.photography:
            total_photography_cost = booking.photography.photography_cost

        # Venue cost (assuming it's a fixed cost per booking)
        venue_cost = booking.venue_name.cost_per_day

        # Calculate the grand total
        booking.grand_total = (
            total_dishes_cost +
            total_drinks_cost +
            total_entertainment_cost +
            total_photography_cost +
            venue_cost
        )

    # Pass the bookings with calculated grand_total to the template
    return render(request, 'booking_payment_page2.html', {'booking': bookings})


def admin_booking_payment_page2(request):
    bookings = Book_Event.objects.all()
    creditcards = Creditcard.objects.all()
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        name_on_card = request.POST.get('name_on_card')
        month = request.POST.get('month')
        year = request.POST.get('year')
        cvv = request.POST.get('cvv')

        creditcard = Creditcard(
            card_number=card_number,
            name_on_card=name_on_card,
            month=month,
            year=year,
            cvv=cvv,
        )

        creditcard.save()
        messages.success(request, "Payment Successfully done. Please wait for some minutes while your booking is being processed")
        return redirect('booking_history')


    # Calculate the grand total for each booking and store it in the booking instance
    for booking in bookings:
        # Get the number of guests
        number_of_guests = booking.number_of_guests

        # Calculate the costs for dishes
        total_dishes_cost = 0
        for dish in [booking.dish1, booking.dish2, booking.dish3]:
            if dish:
                total_dishes_cost += dish.cost_of_dish * number_of_guests

        # Calculate the costs for drinks
        total_drinks_cost = 0
        for drink in [booking.drinks1, booking.drinks2, booking.drinks3, booking.drinks4]:
            if drink:
                total_drinks_cost += drink.drinks_cost * number_of_guests

        # Calculate the costs for entertainment
        total_entertainment_cost = 0
        for entertainment in [booking.entertainment1, booking.entertainment2, booking.entertainment3]:
            if entertainment:
                total_entertainment_cost += entertainment.entertainment_cost

        # Calculate the cost for photography
        total_photography_cost = 0
        if booking.photography:
            total_photography_cost = booking.photography.photography_cost

        # Venue cost (assuming it's a fixed cost per booking)
        venue_cost = booking.venue_name.cost_per_day

        # Calculate the grand total
        booking.grand_total = (
            total_dishes_cost +
            total_drinks_cost +
            total_entertainment_cost +
            total_photography_cost +
            venue_cost
        )

    # Pass the bookings with calculated grand_total to the template
    return render(request, 'admin_booking_payment_page2.html', {'booking': bookings, 'creditcards':creditcards})
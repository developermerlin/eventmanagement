
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    
    path('event/',views.event, name='event'),
    path('edit_event/<int:pk>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:pk>/', views.delete_event, name='delete_event'),
    
    path('dish/', views.dish, name='dish'),
    path('edit_dish/<int:pk>/',views.edit_dish, name='edit_dish'),
    path('delete_dish/<int:pk>/',views.delete_dish, name='delete_dish'),
    
    path('drinks/', views.drinks, name='drinks'),
    path('edit_drinks/<int:pk>/',views.edit_drinks, name='edit_drinks'),
    path('delete_drinks/<int:pk>/',views.delete_drinks, name='delete_drinks'),
    
    path('entertainment/', views.entertainment, name='entertainment'),
    path('edit_entertainment/<int:pk>/',views.edit_entertainment, name='edit_entertainment'),
    path('delete_entertainment/<int:pk>/',views.delete_entertainment, name='delete_entertainment'),
    
    path('photography/', views.photography, name='photography'),
    path('edit_photography/<int:pk>/',views.edit_photography, name='edit_photography'),
    path('delete_photography/<int:pk>/',views.delete_photography, name='delete_photography'),
    
    path('venue/', views.venue, name='venue'),
    path('edit_venue/<int:venue_id>/', views.edit_venue, name='edit_venue'),
    path('delete_venue/<int:venue_id>/', views.delete_venue, name='delete_venue'),
    path('view_venue/<int:venue_id>/', views.view_venue, name='view_venue'),

    path('booking_venue/', views.booking_venue, name='booking_venue'),
    path('booking_venue/edit/<int:booking_venue_id>/', views.edit_booking_venue, name='edit_booking_venue'),
    path('booking_venue/delete/<int:booking_venue_id>/', views.delete_booking_venue, name='delete_booking_venue'),

    path('available_venue/', views.available_venue, name='available_venue'),
    path('available_venue_details/<int:pk>/', views.available_venue_details, name='available_venue_details'),

    path('booking_history/', views.booking_history, name='booking_history'),
    path('booking_history_details/<int:pk>/', views.booking_history_details, name='booking_history_details'),

    path('book_event/', views.book_event, name='book_event'),

    path('admin_booking_history/', views.admin_booking_history, name='admin_booking_history'),
    path('admin_booking_history_details/<int:pk>/', views.admin_booking_history_details, name='admin_booking_history_details'),
    path('edit_payment_status/<int:booking_id>/', views.edit_payment_status, name='edit_payment_status'),

    path('print_receipt/<int:booking_id>/', views.print_receipt, name='print_receipt'),

    path('receipt/<int:booking_id>/', views.receipt, name='receipt'),

    path('booking_payment/', views.booking_payment, name='booking_payment'),

    path('booking_payment_page/', views.booking_payment_page, name='booking_payment_page'),
    path('booking_payment_process/<int:booking_id>/', views.booking_payment_process, name='booking_payment_process'),

    path('booking_payment_page2/', views.booking_payment_page2, name='booking_payment_page2'),


    path('admin_booking_payment_page/', views.admin_booking_payment_page, name='admin_booking_payment_page'),
    path('admin_afrimoney/<int:pk>/', views.admin_afrimoney_detail, name='admin_afrimoney_detail'),

    path('admin_booking_payment_page2/', views.admin_booking_payment_page2, name='admin_booking_payment_page2'),
 


    






]
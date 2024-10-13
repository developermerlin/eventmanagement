
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
]
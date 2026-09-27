from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    # Read (List)
    path('', views.event_list, name='event_list'),
    path('events/', views.event_list, name='event_list_alias'),
    
    # Create
    path('events/add/', views.event_create, name='event_create'),
    path('event/create/', views.event_create, name='event_create_alias'),
    
    # Read (Detail)
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/', views.event_detail, name='event_detail_alias'),
    
    # Update
    path('events/<int:pk>/edit/', views.event_update, name='event_update'),
    path('event/<int:pk>/edit/', views.event_update, name='event_update_alias'),
    
    # Delete
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete_alias'),
]
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'location', 'organizer', 'capacity')
    list_filter = ('start_time', 'organizer')
    search_fields = ('title', 'description', 'location', 'organizer')
    ordering = ('-start_time',)
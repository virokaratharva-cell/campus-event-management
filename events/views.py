from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Event
from .forms import EventForm

def event_list(request):
    """READ: Display all events with optional search and summary statistics."""
    query = request.GET.get('q', '').strip()
    all_events = Event.objects.all()
    events = all_events
    if query:
        events = events.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(organizer__icontains=query)
        )
    
    total_events = all_events.count()
    total_capacity = sum(e.capacity for e in all_events)
    total_locations = all_events.values('location').distinct().count()

    context = {
        'events': events,
        'query': query,
        'total_events': total_events,
        'total_capacity': total_capacity,
        'total_locations': total_locations,
    }
    return render(request, 'events/event_list.html', context)

def event_detail(request, pk):
    """READ: Display single event details."""
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    """CREATE: Add a new event."""
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('events:event_list')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Create New Event'})

def event_update(request, pk):
    """UPDATE: Edit an existing event."""
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('events:event_list')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Edit Event', 'event': event})

def event_delete(request, pk):
    """DELETE: Remove an event after confirmation."""
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        title = event.title
        event.delete()
        messages.success(request, f'Event "{title}" was successfully deleted.')
        return redirect('events:event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})
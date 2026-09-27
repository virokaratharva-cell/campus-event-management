from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from .models import Event
from .serializers import EventSerializer

app_name = 'events_api'

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='api_event')

urlpatterns = router.urls
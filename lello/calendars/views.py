from django.shortcuts import render
from rest_framework import viewsets

from calendars.models import Calendar, Event
from calendars.serializers import CalendarSerializer, EventSerializer


class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

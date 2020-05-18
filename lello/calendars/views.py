from django.shortcuts import render
from rest_framework import viewsets

from calendars.models import Calendar, Event
from calendars.serializers import CalendarSerializer, EventSerializer
from users.permissions import APIPermissionClassFactory


class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CalendarPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'update': True,
                    'partial_update': True,
                    'destroy': True,
                }
            }
        ),
    )

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'update': True,
                    'partial_update': True,
                    'destroy': True,
                }
            }
        ),
    )

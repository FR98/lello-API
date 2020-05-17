from django.shortcuts import render
from rest_framework import viewsets

from checklists.models import Checklist, Element
from checklists.serializers import ChecklistSerializer, ElementSerializer


class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

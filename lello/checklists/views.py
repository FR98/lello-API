from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from checklists.models import Checklist, Element
from checklists.serializers import ChecklistSerializer, ElementSerializer
from users.permissions import APIPermissionClassFactory


class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ChecklistPermission',
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
                    'elements': True,
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        checklist = self.get_object()
        elements = checklist.element_set.all()

        return Response(
            [ElementSerializer(element).data for element in elements]
        )

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ElementPermission',
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

from django.shortcuts import render
from rest_framework import viewsets

from boards.models import Board, List, Card, Label
from boards.serializers import BoardSerializer, ListSerializer, CardSerializer, LabelSerializer
from users.permissions import APIPermissionClassFactory


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BoardPermission',
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

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ListPermission',
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

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CardPermission',
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

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='LabelPermission',
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

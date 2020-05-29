from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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
                    'lists': True,
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def lists(self, request, pk=None):
        board = self.get_object()
        lists = board.list_set.all()

        return Response(
            [ListSerializer(lista).data for lista in lists]
        )

    # def perform_create(self, serializer):
    #     print("HOLA")
    #     return Response(serializer.data)

    # def perform_create(self, serializer):
    #     parent = self.request.user
    #     baby = serializer.validated_data['baby']
    #     if baby.parent.id == parent.id:
    #         event = serializer.save()
    #         return Response(serializer.data)
            
    #     # Retornar error
    #     return Response(serializer.data)

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
                    'cards': True,
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def cards(self, request, pk=None):
        lista = self.get_object()
        cards = lista.card_set.all()

        return Response(
            [CardSerializer(card).data for card in cards]
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

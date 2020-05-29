from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from users.models import UserDetail, Team
from users.serializers import UserSerializer, UserDetailSerializer, TeamSerializer
from users.permissions import APIPermissionClassFactory
from boards.serializers import BoardSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
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

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='UserDetailPermission',
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

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TeamPermission',
            permission_configuration={
                'base': {
                    'create': True, # lambda user, req: user.is_authenticated,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'update': True,
                    'partial_update': True,
                    'destroy': True,
                    'boards': True,
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def boards(self, request, pk=None):
        team = self.get_object()
        boards = team.board_set.all()

        return Response(
            [BoardSerializer(board).data for board in boards]
        )

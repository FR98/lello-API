from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from django.core.mail import send_mail

from users.serializers import UserSerializer, UserDetailSerializer, TeamSerializer
from notifications.serializers import NotificationSerializer
from users.permissions import APIPermissionClassFactory
from boards.serializers import BoardSerializer
from notifications.models import Notification
from django.contrib.auth.models import User
from users.models import UserDetail, Team
from audits.models import Audit

def index(request):
    print("as")
    send_mail(
        'Prueba sujeto',
        'Este es un mensaje',
        'lelloinc@hotmail.com',
        ['gian.luca.99@hotmail.com'],
        fail_silently=False
    )
    print("de")
    return render(request, 'send/index.html')

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
                    'notifications': True,
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def notifications(self, request, pk=None):
        user = self.get_object()
        notifications = Notification.objects.filter(receiver = user)

        return Response(
            [NotificationSerializer(notification).data for notification in notifications]
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
                    'members': True,
                }
            }
        ),
    )

    def create(self, request):
        Audit.objects.create(
            httpMethod = request.method,
            url = '/teams/',
            user = request.user
        )
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            Audit.objects.create(
                httpMethod = request.method,
                url = '/teams/{}/'.format(kwargs['pk']),
                user = request.user
            )
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def boards(self, request, pk=None):
        team = self.get_object()
        boards = team.board_set.all()

        return Response(
            [BoardSerializer(board).data for board in boards]
        )

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        team = self.get_object()
        members = team.members.all()

        return Response(
            [UserSerializer(user).data for user in members]
        )

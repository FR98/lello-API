from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from django.core.mail import EmailMessage
from guardian.shortcuts import assign_perm

from users.serializers import UserSerializer, UserDetailSerializer, TeamSerializer
from notifications.serializers import NotificationSerializer
from users.permissions import APIPermissionClassFactory
from boards.serializers import BoardSerializer
from notifications.models import Notification
from django.contrib.auth.models import User
from users.models import UserDetail, Team
from audits.models import Audit

def index(request):
    # email = EmailMessage(
    #     'Hello from Lello',
    #     'Message',
    #     'lellodjango@gmail.com',
    #     ['frangrosalo@hotmail.com'],
    # )
    # email.send(fail_silently=False)
    send_email('Hola', ['frangrosalo@hotmail.com'])
    return render(request, 'send/index.html')

def send_email(message, to):
    EmailMessage(
        'Hello from Lello',
        message,
        'lellodjango@gmail.com',
        to,
        index.html,
    ).send(fail_silently=False)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'update': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'destroy': lambda user, obj, req: user.is_authenticated,
                    'notifications': lambda user, obj, req: user.is_authenticated,
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
                    'list': False,
                },
                'instance': {
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'update': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'destroy': lambda user, obj, req: user.is_authenticated,
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
                    'create': lambda user, req: user.is_authenticated,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'update': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'destroy': 'users.delete_team',
                    'boards': lambda user, obj, req: user.is_authenticated,
                    'members': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        user = self.request.user
        team = serializer.save()
        assign_perm('users.delete_team', user, team)
        Audit.objects.create(
            httpMethod = self.request.method,
            url = '/teams/',
            user = user
        )
        return Response(serializer.data)

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

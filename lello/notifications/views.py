from django.shortcuts import render
from rest_framework import viewsets, status
from django.http import Http404
from rest_framework.response import Response

from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from users.permissions import APIPermissionClassFactory
from audits.models import Audit


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='NotificationPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'update': False,
                    'partial_update': False,
                    'destroy': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def create(self, request):
        Audit.objects.create(
            httpMethod = request.method,
            url = '/notifications/',
            user = request.user
        )
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            Audit.objects.create(
                httpMethod = request.method,
                url = '/notifications/{}/'.format(kwargs['pk']),
                user = request.user
            )
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

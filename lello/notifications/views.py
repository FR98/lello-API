from django.shortcuts import render
from rest_framework import viewsets, status
from django.http import Http404

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

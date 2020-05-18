from django.shortcuts import render
from rest_framework import viewsets

from audits.models import Audit
from audits.serializers import AuditSerializer
from users.permissions import APIPermissionClassFactory


class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='AuditPermission',
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

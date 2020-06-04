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
                    'create': False,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'update': False,
                    'partial_update': False,
                    'destroy': False,
                }
            }
        ),
    )

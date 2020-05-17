from django.shortcuts import render
from rest_framework import viewsets

from audits.models import Audit
from audits.serializers import AuditSerializer


class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer

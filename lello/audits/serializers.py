from rest_framework import serializers

from audits.models import Audit


class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = '__all__'

from rest_framework import serializers

from audits.models import Audit
from users.serializers import UserSerializer


class AuditSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Audit
        fields = '__all__'

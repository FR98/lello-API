from rest_framework import serializers

from django.contrib.auth.models import User
from users.models import UserDetail, Team



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'username'
        )

    


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

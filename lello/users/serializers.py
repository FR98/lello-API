from rest_framework import serializers

from django.contrib.auth.models import User
from users.models import UserDetail, Team
from users.services import enviar_email


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password'
        )

    # detail = UserDetailSerializer(many=False, read_only=False)
    def create(self, validated_data):
        try:
            email = validated_data["email"]
            enviar_email([email], 'Bienvenido! Te has registrado en Lello')
        except:
            print("Email failed :(")
        
        user = User.objects.create_user(**validated_data)
        # user = User.objects.create(
        #     user = validated_data["username"],
        #     active = True
        # )
        # user.set_password(validated_data["password"])
        # user.save()
        return user


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

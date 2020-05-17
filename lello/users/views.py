from django.shortcuts import render
from rest_framework import viewsets

from django.contrib.auth.models import User
from users.models import UserDetail, Team
from users.serializers import UserSerializer, UserDetailSerializer, TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

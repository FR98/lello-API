from rest_framework import serializers

from boards.models import Board, List, Card, Label
from users.serializers import TeamSerializer, UserSerializer
from checklists.serializers import ChecklistSerializer


class BoardSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    owner = UserSerializer()

    class Meta:
        model = Board
        fields = '__all__'

    # def create(self, validated_data):
    #     team_data = validated_data.pop('team')
    #     board = Board.objects.create(**validated_data)
    #     return board

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    checklist = ChecklistSerializer()
    label = LabelSerializer()
    assigned_to = UserSerializer(many=True)

    class Meta:
        model = Card
        fields = '__all__'

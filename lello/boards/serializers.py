from rest_framework import serializers

from boards.models import Board, List, Card, Label
from users.serializers import TeamSerializer, UserSerializer
from checklists.serializers import ChecklistSerializer
from calendars.models import Calendar


class BoardSerializer(serializers.ModelSerializer):
    # team = TeamSerializer()
    # owner = UserSerializer(read_only = True)
    # calendar = CalendarSerializer()

    class Meta:
        model = Board
        fields = '__all__'

    def create(self, validated_data):
        # calendar_date = validated_data.pop('calendar')
        board = Board.objects.create(**validated_data)
        Calendar.objects.create(
            board = board
        )
        return board

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    # checklist = ChecklistSerializer(read_only=True)
    # label = LabelSerializer(read_only=True)
    # assigned_to = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    card_set = CardSerializer(many=True, read_only=True)
    class Meta:
        model = List
        fields = '__all__'

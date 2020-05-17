from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name =  models.CharField(
        max_length = 50,
        null = False, 
        blank = False
    )
    descriptiom = models.CharField(
        max_length = 200,
        null = True,
        blank = True
    )
    owner = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    is_private = models.BooleanField(
        default = False
    )

    def __str__(self):
        return self.name

class Member(models.Model):
    board = models.ForeignKey(
        'boards.Board',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    role = models.ForeignKey(
        'boards.Role',
        null = True,
        blank = True,
        on_delete = models.SET_NULL
    )

    def __str__(self):
        return self.user

class Role(models.Model):
    name = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(
        max_length = 20,
        null = False,
        blank = False
    )
    hours_estimated = models.DecimalField(
        decimal_places = 2
    )
    hours_done = models.DecimalField(
        decimal_places = 2
    )

class Card(models.Model):
    name = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )
    number = models.IntegerField()
    description = models.CharField(
        max_length = 200,
        null = True,
        blank = True
    )
    hours_estimated = models.DecimalField(
        decimal_places = 2
    )
    hours_done = models.DecimalField(
        decimal_places = 2
    )
    checklist = models.ForeignKey(
        'checklists.Checklist',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    deadline = models.DateTimeField(
        null = True,
        blank = True
    )
    label = models.ForeignKey(
        'boards.Label',
        null = True,
        blank = True,
        on_delete = models.SET_NULL
    )

    def __str__(self):
        return self.number + self.name
    
class Label(models.Model):
    name = models.CharField(
        max_length = 20,
        null = False,
        blank = False
    )
    color = models.CharField(
        max_length = 10
    )

    def __str__(self):
        return self.name

# m2m
class Assigned(models.Model):
    card = models.ForeignKey(
        'boards.Card',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.card + self.user

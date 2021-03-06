from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from users.models import Team


class Board(models.Model):
    name =  models.CharField(
        max_length = 50,
        null = False, 
        blank = False
    )
    descriptiom = models.CharField(
        max_length = 200,
        null = True,
    )
    owner = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE,
        related_name = "owner"
    )
    is_private = models.BooleanField(
        default = False
    )
    team = models.ForeignKey(
        Team,
        null = False,
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(
        max_length = 20,
        null = False,
        blank = False
    )
    board = models.ForeignKey(
        Board,
        null = False,
        on_delete = models.CASCADE,
    )
    hours_estimated = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
        default = 0,
    )
    hours_done = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
        default = 0,
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.name

class Card(models.Model):
    title = models.CharField(
        max_length = 75,
        null = False,
        blank = False
    )
    lista = models.ForeignKey(
        List,
        null = False,
        on_delete = models.CASCADE,
    )
    number = models.IntegerField(null=True)
    description = models.CharField(
        max_length = 300,
        null = True,
    )
    hours_estimated = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
        default = 0,
    )
    hours_done = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
        default = 0,
    )
    deadline = models.DateTimeField(
        null = True,
    )
    label = models.ForeignKey(
        'boards.Label',
        null = True,
        on_delete = models.SET_NULL
    )
    assigned_to = models.ManyToManyField( User, blank = True )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.title
    
class Label(models.Model):

    class Priority(models.TextChoices):
        high 	= 'H', _('High')
        medium 	= 'M', _('Medium')
        low     = 'L', _('Low')
    
    name = models.CharField(
        max_length = 20,
        null = False,
    )
    color = models.CharField(
        max_length = 10,
        default = '#ffffff'
    )
    priority = models.CharField(
        choices = Priority.choices,
        max_length = 20,
        editable = True,
        default = 'L',
    )

    def __str__(self):
        return self.name

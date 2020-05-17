from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


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
    members = models.ManyToManyField( User )
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
    hours_estimated = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
    )
    hours_done = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
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
    number = models.IntegerField()
    description = models.CharField(
        max_length = 300,
        null = True,
    )
    hours_estimated = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
    )
    hours_done = models.DecimalField(
        decimal_places = 2,
        max_digits = 4,
    )
    checklist = models.ForeignKey(
        'checklists.Checklist',
        null = True,
        on_delete = models.SET_NULL
    )
    deadline = models.DateTimeField(
        null = True,
    )
    label = models.ForeignKey(
        'boards.Label',
        null = True,
        on_delete = models.SET_NULL
    )
    assigned_to = models.ManyToManyField( User )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.number + " " + self.title
    
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

from django.db import models
from django.contrib.auth.models import User

class Action(models.Model):
    name = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )

    def __str__(self):
        return self.name

class Notification(models.Model):
    title = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )
    description = models.CharField(
        max_length = 250,
        null = True,
        blank = True
    )
    datetime = models.DateTimeField(
        null = True
    )
    transmitter = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.title



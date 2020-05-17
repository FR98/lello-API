from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    title = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )
    description = models.CharField(
        max_length = 250,
        null = True,
    )
    transmitter = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE,
        related_name = 'transmitter',
    )
    receiver = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE,
        related_name = 'receiver',
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User


class Audit(models.Model):
    date = models.DateField(
        null = True
    )
    time = models.TimeField(
        null = True
    )
    action = models.ForeignKey(
        'actions.Action',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    entity = models.CharField(
        max_length = 50,
        null = True,
        blank = True,
    )
    httpType = models.CharField(
        max_length = 100,
        null = True,
        blank = True
    )
    url = models.URLField(
        null = True
    )
    user = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.action

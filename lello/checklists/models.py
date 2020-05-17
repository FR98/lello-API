from django.db import models
from django.contrib.auth.models import User



class Checklist(models.Model):
    name = models.CharField(
        max_length = 50,
        blank = True,
        null = True
    )

    def __str__(self):
        return self.name

class Element(models.Model):
    title = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )
    checklist = models.ForeignKey(
        'checklists.Checklist',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    position = models.IntegerField()
    is_done = models.BooleanField(
        default = False
    )
    assigned_to = models.ForeignKey(
        User,
        null = True,
        blank = True,
        on_delete = models.SET_NULL
    )
    deadline = models.DateTimeField(
        null = True
    )

    def __str__(self):
        return self.title

from django.db import models


class Calendar(models.Model):
    board = models.ForeignKey(
        'boards.Board',
        null = False,
        blank = False,
        on_delete = models.CASCADE 
    )
    
class Event(models.Model):
    calendar = models.ForeignKey(
        'calendars.Calendar',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    title = models.CharField(
        max_length = 150,
        null = False,
        blank = False
    )
    description = models.CharField(
        max_length = 250,
        null = True,
    )
    url = models.URLField(
        null = True
    )
    date = models.DateTimeField(
        null = False,
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.title

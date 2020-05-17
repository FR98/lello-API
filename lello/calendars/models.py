from django.db import models


class Calendar(models.Model):
    board = models.ForeignKey(
        'boards.Board',
        null = False,
        blank = False,
        on_delete = models.CASCADE 
    )

    def __str__(self):
        return self.board
    
class Event(models.Model):
    calendar = models.ForeignKey(
        'calendars.Calendar',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    date = models.DateField(
        null = False
    )
    title = models.CharField(
        max_length = 150,
        null = False,
        blank = False
    )
    description = models.CharField(
        maxlength = 250,
        null = True, 
        blank = True
    )
    url = models.URLField(
        null = True
    )

    def __str__(self):
        return self.title

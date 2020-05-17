from django.db import models

class Board(models.Model):
    class Board(models.Model):
        name =  models.CharField(
            max_length = 20,
            null = False, 
            blank = False
        )
        descriptiom = models.CharField(
            max_length = 200,
            null = True,
            blank = True
        )
        owner = models.ForeignKey(
            'users.User',
            null = False,
            blank = False,
            on_delete = models.CASCADE
        )
        # TODO: Revisar, foreignkey??
        privacy = models.IntegerField()

        def __str__(self):
            return self.name

    class Member(models.Model):
        board = models.ForeignKey(
            # TODO: REVISAR
            'boards.Board',
            null = False,
            blank = False,
            on_delete = models.SET_NULL
        )
        user = models.ForeignKey(
            # TODO: REVISAR
            'users.User',
            null = False,
            blank = False,
            on_delete = models.SET_NULL
        )
        # TODO: REVISAR
        role = models.ForeignKey(
            'boards.Role',
            null = False,
            blank = False,
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
        # hours ?

    class Card(models.Model):
        name = models.CharField(
            max_length = 20,
            null = False,
            blank = False
        )
        number = models.IntegerField()
        description = models.CharField(
            max_length = 200,
            null = True,
            blank = True
        )
        # hours ?
        checklist = models.ForeignKey(
            # TODO: REVISAR
            'checklists.Checklist',
            null = False,
            blank = False,
            on_delete = models.CASCADE
        )
        deadline = models.DateField(
            null = True,
            blank = True
        )
        label = models.ForeignKey(
            'boards.Label',
            null = False,
            blank = False,
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
            'users.User',
            null = False,
            blank = False,
            on_delete = models.CASCADE
        )

        def __str__(self):
            return self.card + self.user

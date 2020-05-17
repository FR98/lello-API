from django.db import models


class User(models.Model):
    class UserDetail(models.Model):
        user = models.CharField(
            max_length = 50, 
            null = False, 
            blank = False
            )
        gender = models.CharField(
            max_length = 10,
            null=True,
            blank=True
        )
        phone = models.CharField(
            max_length = 8,
            null = True,
            blank = True
        )
        birthdate = models.DateField(
            null = False
        )

        def __str__(self):
            return self.user

    class Team(models.Model):
        name = models.CharField(
            max_length = 50,
            null = False,
            blank = False
        )

        def __str__(self):
            return self.name

    class UserTeam(models.Model):
        team = models.ForeignKey(
            # TODO: Revisar foreign key
            'users.Team',
            null = False,
            blank = False,
            on_delete = models.CASCADE
        )
        user = models.ForeignKey(
            # TODO: Revisar foreign key
            'users.User',
            null = False,
            blank = False,
            on_delete = models.CASCADE
        )
        role = models.ForeignKey(
            # TODO: Revisar foreign key
            'users.Role',
            null = False,
            blank = False,
            on_delete = models.CASCADE
        )

        def __str__(self):
            return self.team

    class Role(models.Model):
        name = models.CharField(
            max_length = 20,
            null = False,
            blank = False
        )

        def __str__(self):
            return self.name
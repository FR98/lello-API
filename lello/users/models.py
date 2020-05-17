from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):

    class Gender(models.TextChoices):
        male 	= 'M', _('Male')
        female 	= 'F', _('Female') 
        
    user = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    # TODO: enum
    gender = models.CharField(
        choices = Gender.choices
        max_length = 10,
        editable = False,
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
        'users.Team',
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    role = models.ForeignKey(
        'users.Role',
        null = True,  
        on_delete = models.SET_NULL
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
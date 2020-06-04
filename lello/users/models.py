from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserDetail(models.Model):

    # class Gender(models.TextChoices):
    #     male 	= "M", _("Male")
    #     female 	= "F", _("Female")
    
    # user = models.ForeignKey(
    #     User,
    #     null = False,
    #     blank = False,
    #     on_delete = models.CASCADE
    # )
    user = models.ForeignKey(
        User, 
        # related_name="detail",
        on_delete= models.CASCADE
    )
    gender = models.CharField(
        # choices = Gender.choices,
        max_length = 10,
        # editable = False,
        null = False,
    )
    phone = models.CharField(
        max_length = 8,
        null = True,
    )
    birthdate = models.DateField(
        null = True
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return User.objects.get( pk = self.user ).first_name

class Team(models.Model):
    name = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )
    description = models.CharField(
        max_length = 200,
        null = True,
    )
    members = models.ManyToManyField(
        User,
        through = 'users.Member',
        related_name = "members",
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.name

class Member(models.Model):
    team = models.ForeignKey(
        'users.Team',
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    joined_at = models.DateTimeField(
        auto_now_add = True
    )
    # role = models.ForeignKey(
    #     'users.Role',
    #     null = True,  
    #     on_delete = models.SET_NULL
    # )

# class Role(models.Model):
#     name = models.CharField(
#         max_length = 20,
#         null = False,
#         blank = False
#     )

#     def __str__(self):
#         return self.name

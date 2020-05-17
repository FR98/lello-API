from django.db import models

# Create your models here.
class Checklist(models.Model):
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
        # TODO: Revisar foreign key
        checklist = models.ForeignKey(
            'checklists.Checklist',
            null = False,
            blank = False,
            on_delete = models.SET_NULL
        )
        position = models.CharField(
            max_length = 20, 
            null = False,
            blank = False
        )
        is_done = models.BooleanField(
            default = False
        )
        # TODO: Revisar tipo de dato
        assigned = models.BooleanField(
            default = False
        )
        deadline = models.DateField(
            null = True
        )

        def __str__(self):
            return self.title

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Audit(models.Model):

    class HttpType(models.TextChoices):
        GET 	= 'GET',    _('GET')
        POST 	= 'POST',   _('POST')
        PUT     = 'PUT',    _('PUT')
        DELETE  = 'DELETE', _('DELETE')
    
    httpType = models.CharField(
        choices = HttpType.choices,
        max_length = 20,
        editable = False,
        default = 'GET',
    )
    url = models.CharField(
        max_length = 300,
    )
    user = models.ForeignKey(
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )

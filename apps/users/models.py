from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255, unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def validate_user(sender, instance, **kwargs):
    err = ''
    if len(instance.first_name) < 5:
        err += 'First name must be at least 5 characters'
    if not EMAIL_REGEX.match(instance.email_address):
        err += 'Email must be a valid address'
    if err:
        from django.core.exceptions import ValidationError
        raise ValidationError(err)
        
        
models.signals.pre_save.connect(validate_user, sender=User)         

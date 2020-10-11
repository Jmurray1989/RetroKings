from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):
    """
    Contact Model
    """
    name = models.CharField(max_length=200)
    message = models.TextField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

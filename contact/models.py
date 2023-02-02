
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.TextField()
    sub = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name

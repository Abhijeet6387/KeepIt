from django.db import models

# Create your models here.

# python class - models
class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    # whenever we save a note, auto_now will save a timestamp 
    updated = models.DateTimeField(auto_now=True)
    # whenever we create a note, auto_now_add will save a timestamp
    created = models.DateTimeField(auto_now_add=True)

    # creating a string representation
    def __str__(self):
        return self.body[0:50] # first 50 character

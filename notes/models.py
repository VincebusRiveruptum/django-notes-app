from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.TextField()
    body = models.TextField()
    highlight = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

class Book(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()


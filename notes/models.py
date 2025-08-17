from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    highlight = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 
    # Django already solves this... so it is not necessary
    #def notes(self):
    #    return self.notes.all()

class Note(models.Model):
    book = models.ForeignKey(Book, related_name=("notes"), on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField(null=True)
    body = models.TextField()
    highlight = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # set later
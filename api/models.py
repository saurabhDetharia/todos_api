from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
    
class Todo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500, editable=True, blank=True)
    isCompleted = models.BooleanField()
    
    def __str__(self):
        return self.title

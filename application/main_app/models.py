from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=20)
    PRIORITIES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('R', 'Major'),
        ('C', 'Critical')
    )
    species = models.TextField()
    age = models.IntegerField()
    description = models.TextField()
    priority = models.CharField(max_length=1, choices=PRIORITIES)

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    duration = models.FloatField()  # Duration in hours

    def __str__(self):
        return self.title
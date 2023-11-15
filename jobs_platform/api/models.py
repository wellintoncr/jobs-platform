from django.db import models

# Create your models here.
class Job(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField()
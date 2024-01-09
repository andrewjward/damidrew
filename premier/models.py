from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120)
    rank = models.PositiveBigIntegerField()

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(1)
    buyer = models.ManyToManyField(Buyer, related_name='games')
    DecimalField = models.FloatField()
    BooleanField = models.BooleanField(1)

    def __str__(self):
        return self.title

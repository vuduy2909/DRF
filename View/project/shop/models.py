# blog/models.py
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

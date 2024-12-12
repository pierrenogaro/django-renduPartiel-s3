from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
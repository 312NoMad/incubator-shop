from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title

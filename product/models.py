from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    cost = models.DecimalField(max_digits=6, decimal_places=1)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

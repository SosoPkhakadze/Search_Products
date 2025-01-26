from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    source = models.CharField(max_length=100)
    source_url = models.URLField()

    def __str__(self) -> str:
        return self.title
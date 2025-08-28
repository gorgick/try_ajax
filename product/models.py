from django.db import models


class Product(models.Model):
    STATUS_CHOICES = (
        ("A", "Perfect"),
        ("B", "Good"),
        ("C", "NotBad"),
        ("D", "Bad"),
    )
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=99.99)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="B"
    )
    amount = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

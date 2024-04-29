from django.db import models
from django.contrib.auth.models import User

class Bike(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)

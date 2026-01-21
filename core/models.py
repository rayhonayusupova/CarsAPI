from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number=models.CharField(max_length=20)

class Car(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=80)
    year=models.PositiveIntegerField()
    mileage=models.PositiveIntegerField()
    engine_power=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    
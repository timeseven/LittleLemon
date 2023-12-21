from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.


class Menu(models.Model):
    id = models.IntegerField(primary_key=True, validators=[
                             MaxValueValidator(99999)])
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(99999)])


class Booking(models.Model):
    id = models.BigIntegerField(primary_key=True, validators=[
                                MaxValueValidator(99999999999)])
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(999999)])
    bookingDate = models.DateField()

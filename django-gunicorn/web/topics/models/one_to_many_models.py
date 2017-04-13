from django.db import models


class Manufacturer(models.Model):
    """
    Example for a many-to-one relationship:
    - Manufacturer
    - Cars

    -> Each car has only one manufacture
    -> Each manufacturer produces many cars
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

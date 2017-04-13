from django.db import models
from .regular_models import Person


class CollegeCommon(models.Model):
    """
    This model represents an abstract base class.
    Abstract base classes don't generate any database tables,
    but instead can be used by other models that will inherit
    the fields defined in this class.
    """
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CollegeCommon):
    """
    Child class that uses CollegeCommon as a base class.
    """
    home_group = models.CharField(max_length=5)


class Place(models.Model):
    """
    This is the parent model using multi-table inheritance.
    Any child classes (e.g. Restaurant) will be linked
    to the parent class by using a OneToOneField link.
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    def __str__(self):
        return self.name

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class OrderedPerson(Person):
    """
    Proxy models are used when the fields of a model will
    generally NOT be changed, but instead it's just required to
    add a method, define a different default manager, or change
    other Meta properties.

    The below example will create a new Model that is a proxy
    model. The only difference is the sorting for the model
    list.
    """

    class Meta:
        proxy = True
        ordering = ['first_name']

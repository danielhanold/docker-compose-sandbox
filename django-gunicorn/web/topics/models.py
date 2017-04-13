from django.db import models
from datetime import date

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZES,
        default='M'
    )
    birthday = models.DateField('birthday', default=date.today)

    def baby_boomer_status(self):
        """
        Determine if this person is a baby boomer.
        :return: String
        """
        import datetime
        if self.birthday < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birthday < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        """Returns the person's full name."""
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return " ".join([self.first_name, self.last_name])

    class Meta:
        # Define a verbose pluralized name.
        verbose_name_plural = "people"


class Musician(models.Model):
    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    def __str__(self):
        return self.name

    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    # Add choices organized into groups.
    MEDIA_CHOICES = (
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        (None, 'Unknown'),
    )
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_CHOICES,
        default='cd',
        help_text='If you still use anything but CDs, then you are super cool.'
    )


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


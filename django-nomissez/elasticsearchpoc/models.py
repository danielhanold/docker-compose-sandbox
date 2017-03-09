from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class Author(models.Model):
	id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email_alias = models.CharField(max_length=120, null=True, blank=True)
	thumbnail = models.CharField(max_length=255, null=True, blank=True)
	title = models.CharField(max_length=120, null=True, blank=True)

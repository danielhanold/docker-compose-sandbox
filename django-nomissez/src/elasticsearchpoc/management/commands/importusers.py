from elasticsearchpoc.models import Author
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):

	def handle(self, *args, **kwargs):

		c = CopyMapping(
		
			#pass in Model
			Author, 
			"./elasticsearchpoc/static/csv/DjangoBioImport.csv",
			dict(id="id", first_name='first_name', last_name='last_name', 
				email_alias='email_alias', thumbnail='thumbnail', 
				title='title')
			)
		c.save()
		
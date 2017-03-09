from django.test import TestCase
from models import Author

# Create your tests here.
class ElasticTestCase(TestCase):
	def setUp(self):
		Author.objects.create(id=1, first_name="simon", last_name="slater",
			email_alias="sslater@dnainfo.com", thumbnail="blank", 
			title="awesome")


	def test_200_response_search_page(self):
		response = self.client.get('/elastic/')
		self.assertEqual(response.status_code, 200)

	def test_can_get_author_by_id(self):
		authorInfo = Author.objects.get(id=1)
		self.assertEqual(authorInfo.last_name, 'slater')

	def test_this_test_will_fail(self):
		self.assertEqual(1, 2)



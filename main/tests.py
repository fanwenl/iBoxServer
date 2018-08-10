from django.test import TestCase
from django.urls import reverse
from . import views

# Create your tests here.
class viewstest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)

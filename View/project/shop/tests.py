# blog/tests.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views


from django.test import SimpleTestCase
from django.urls import reverse

class ErrorViewTests(SimpleTestCase):
    def test_404_custom_page(self):
        response = self.client.get('/non-existent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "404 - Page not found")

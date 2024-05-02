from django.test import TestCase


# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """testa se index roda"""
        response = self.client.get("127.0.0.1:8000")
        self.assertEqual(response.status_code, 200)

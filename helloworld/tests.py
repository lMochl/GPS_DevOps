from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HelloWorldTestCase(TestCase):
    def test_hello_world_view(self):
        url = reverse('helloworld') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
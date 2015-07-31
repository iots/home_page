from django.test import TestCase
from django.test import Client
from .models import Person

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        Person.objects.create(name='online', number=65535)
        Person.objects.create(name='read', number=4096)
        Person.objects.create(name='sent', number=1024)

    def testHomeView(self):
        response = self.client.get('/home_show/home/')
        self.assertEqual(response.status_code, 200)

    def testQueryView(self):
        response = self.client.get('/home_show/query/', follow=True, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        readjson = eval(response.content)
        self.assertEqual(readjson['online'], 65535)
        self.assertEqual(readjson['read'], 4096)
        self.assertEqual(readjson['sent'], 1024)
        self.assertEqual(response.status_code, 200)



from django.test import TestCase
from django.test import Client


from bootcamp.core.tests import UserFactory

class CampTestCase(TestCase):

    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.user = UserFactory(is_staff=True)

    def assertSuccess(self, request):
        self.assertEqual(request.status_code, 200)

    def assertCreated(self, request):
        self.assertEqual(request.status_code, 201)

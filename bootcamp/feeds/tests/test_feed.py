from django.urls import reverse

from . import FeedFactory
from bootcamp.core.tests import UserFactory

from bootcamp.common.test_case import CampTestCase

#pylint: disable=invalid-name
class FeedTestCase(CampTestCase):

    def setUp(self):
        super(FeedTestCase, self).setUp()
        self.feed = FeedFactory(user=self.user)
        self.pwd = UserFactory.create().password

    def test_create_post(self):
        self.client.login(username=self.user.username, password=self.pwd)
        print(self.user.username, self.user.password)

        url = reverse('feeds')
        request = self.client.get(url)
        self.assertSuccess(request)

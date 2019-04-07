import datetime
import factory
import random

from bootcamp.core.tests import UserFactory
from bootcamp.feeds.models import Feed

class FeedFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Feed

    user = factory.SubFactory(UserFactory)
    post = factory.Sequence(lambda n: 'testing post{}'.format(n))

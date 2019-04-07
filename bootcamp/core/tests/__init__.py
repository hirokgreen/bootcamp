import factory

from django.contrib.auth.models import User


# pylint: disable=no-init, old-style-class, too-few-public-methods
class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User
    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda user: '{}@example.com'.format(user.first_name))
    password = factory.PostGenerationMethodCall('set_password', 'testpass')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

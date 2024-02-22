import datetime
import factory
import pytest

from .. import models


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Activity

    domain = factory.Sequence(lambda n: 'example{}.com'.format(n))
    datetime = datetime.datetime.now()

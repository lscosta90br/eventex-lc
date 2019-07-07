from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTes(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Eric Patrick',
            cpf='12345678901',
            email='ericpatrick15@gmail.com',
            phone='62-99685-1234'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Eric Patrick', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False"""
        self.assertFalse(self.obj.paid)
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification

# Create your tests here.
class NotificationTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")

    def test_create_notification(self):
        Notification.objects.create(recipient=self.user1, actor=self.user2, verb="followed you")
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(Notification.objects.first().verb, "followed you")
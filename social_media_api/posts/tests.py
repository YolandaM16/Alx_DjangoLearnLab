from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

# Create your tests here.
class LikePostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(title="Test Post", content="This is a test post", author=self.user)

    def test_like_post(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post(self):
        Like.objects.create(user=self.user, post=self.post)
        self.client.login(username="testuser", password="password")
        response = self.client.delete(f'/posts/{self.post.id}/unlike/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Like.objects.count(), 0)
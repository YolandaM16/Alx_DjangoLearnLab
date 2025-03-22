from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(default=timezone.now)


    def _str_(self):
        return self.title
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(("Bio"), blank=True)
    profile_pic = models.ImageField(("Profile Picture"), upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    


class Comment(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.title}'
    
    class Meta:
        ordering = ['created_date']

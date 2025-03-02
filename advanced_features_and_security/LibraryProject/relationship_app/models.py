from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Member")


class Author(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    class Meta:
        permissions = (
            ("can_add_book", "Can_add_book"),
            ("can_change_book", "Can_change_book"),
            ("can_delete_book", "Can_delete_book")
        )

    def _str_(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def _str_(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True)

    def _str_(self):
        return self.name
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


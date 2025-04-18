from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


    def _str_(self):
        return self.title
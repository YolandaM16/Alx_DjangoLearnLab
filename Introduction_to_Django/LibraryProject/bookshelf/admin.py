from django.contrib import admin
from .models import Book 

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "publication_year"]
    list_filter = ["publication_year", "author"]
    search_fields = ["title", "author"]
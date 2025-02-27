from django.contrib import admin
from .models import Book

# Custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for the publication year and author
    list_filter = ('publication_year', 'author')

    # Enable search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields = '_all_'

        def validate_publication_year(self, value):
            """Ensure the publication year is not in the future."""
            current_year = datetime.datetime.now().year
            if value > current_year:
                raise serializers.ValidationError("Publicaion year can't be in the future.")
            return value
        

class AuthorSerializer(serializers.ModelSerializer):
    books =BookSerializer(many=True, read_only=True) #Nested serializer

    class Meta:
        models = Author
        fields = ['name', 'books']
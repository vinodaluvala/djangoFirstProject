from rest_framework import serializers

from library.models import Book


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors']
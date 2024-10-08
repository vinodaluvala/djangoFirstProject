from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.serializers import bookSerializer, AuthorSerializer


# Create your views here.
@api_view(['POST'])
def create_book(request):
    # serializers are used to convert one type of date to another. here we are receiving json data tp convert books object
    book_serializer = bookSerializer(data=request.data)

    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)
    if author_serializer.is_valid():
        author_serializer.save()

        return Response(author_serializer.data, status=status.HTTP_201_CREATED)

    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
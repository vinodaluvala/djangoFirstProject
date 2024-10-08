from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.serializers import bookSerializer
# Create your views here.
@api_view(['POST'])
def create_book(request):
    # serializers are used to convert one type of date to another. here we are receiving json data tp convert books object
    Book_Serializer = bookSerializer(data=request.data)

    if Book_Serializer.is_valid():
        Book_Serializer.save()
        return Response(Book_Serializer.data, status=status.HTTP_201_CREATED)
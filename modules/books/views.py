from django.shortcuts import render
from rest_framework import generics,filters
from .models import Book
from .serializers import BookSerializer
import django_filters.rest_framework

class ListBook(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
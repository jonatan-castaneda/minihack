from django.shortcuts import render
from rest_framework import generics,filters
from .models import Author
from .serializers import AuthorSerializer
import django_filters.rest_framework

class ListAuthor(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class = AuthorSerializer


class DetailAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
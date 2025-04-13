from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, filters , permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author,Category,Book,Review
from .serializers import AuthorSerializer,CategorySerializer,BookSerializer,ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['name']
    ordering_fields=['name','created_at']
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['name']
    
class BookViewSet(viewsets.ModelViewSet):
      queryset=Book.objects.all()
      serializer_class=BookSerializer
      filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
      filterset_fields = ['author', 'categories', 'in_stock']
      search_fields = ['title', 'isbn', 'author__name', 'description']
      ordering_fields = ['title', 'author__name', 'published_date', 'price', 'created_at'] 
      
class ReviewViewSet(viewsets.ModelViewSet):#just want to add the comment 
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields=['book','user','rating']
    ordering_fields=['created_at','rating']       
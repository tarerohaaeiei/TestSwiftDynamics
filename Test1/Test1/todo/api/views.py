from django.shortcuts import render
from .serializers import ListSerializer
from .models import List
from rest_framework import generics
from rest_framework import generics, permissions

class ListsView(generics.ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
class ListsPost(generics.CreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
    # permission_classes = [permissions.IsAuthenticated]
    
class ListsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
    # permission_classes = [permissions.IsAuthenticated]
    
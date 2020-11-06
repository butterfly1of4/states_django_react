from django.shortcuts import render
from .serializers import StateSerializer
from .models import States
from rest_framework import generics
# Create your views here.

class StateAPI(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer

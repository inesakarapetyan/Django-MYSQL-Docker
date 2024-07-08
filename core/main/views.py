from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HumanSerializer
from .models import Human
# Create your views here.

class HumanViewset(viewsets.ModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

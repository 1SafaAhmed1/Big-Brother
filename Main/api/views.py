from django.shortcuts import render
from rest_framework import generics

from classroom.models import Classroom
from .serializers import ClassroomSerializer

# Create your views here.


class ClassroomAPIView(generics.ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
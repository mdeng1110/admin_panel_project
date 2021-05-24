from django.shortcuts import render

# Create your views here.
...
from django.shortcuts import render
from .models import Instructor
from rest_framework import generics
from .serializers import InstructorSerializer


class InstructorCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Instructor
    queryset = Instructor.objects.all(),
    serializer_class = InstructorSerializer


class InstructorList(generics.ListAPIView):
    # API endpoint that allows Instructor to be viewed.
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Instructor by pk.
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Instructor record to be updated.
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Instructor record to be deleted.
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

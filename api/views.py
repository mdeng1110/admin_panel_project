from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
...
from django.shortcuts import render
from .models import Course, Instructor
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import InstructorSerializer, CourseSerializer

@api_view(['GET'])
def instructor_list(request):
    instructors = Instructor.objects.filter(enabled=True)
    serializer = InstructorSerializer(instructors, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def instructor_describe(request, pk):
    instructor = Instructor.objects.filter(pk=pk)
    serializer = InstructorSerializer(instructor, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def instructor_add(request):
    payload = JSONParser().parse(request)
    serializer = InstructorSerializer(data=payload)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def instructor_update(request, pk):
    instructor = Instructor.objects.get(pk=pk)
    payload = JSONParser().parse(request)
    serializer = InstructorSerializer(instructor, data=payload)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def instructor_remove(request, pk):
    instructor = Instructor.objects.get(pk=pk)
    instructor.delete()
    return JsonResponse({'message': 'Instructor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def course_list(request):
    courses = Course.objects.filter(enabled=True)
    serializer = CourseSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def course_describe(request, pk):
    course = Course.objects.filter(pk=pk)
    serializer = CourseSerializer(course, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def course_add(request):
    payload = JSONParser().parse(request)
    serializer = CourseSerializer(data=payload)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    payload = JSONParser().parse(request)
    serializer = CourseSerializer(course, data=payload)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def course_remove(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return JsonResponse({'message': 'Course was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
from rest_framework import serializers
from .models import Instructor, Course 

class InstructorSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Instructor 
        fields = ['pk', 'username', 'first_name', 'last_name', 'email', 'courses', 'created', 'enabled']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['pk', 'name', 'description', 'instructor', 'created', 'enabled']
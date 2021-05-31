from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class WelcomeView(TemplateView):
    template_name = "home.html"

class StudentView(TemplateView):
    template_name = "students.html"

class InstructorView(TemplateView):
    template_name = "instructors.html"

class StudentOnboardingView(TemplateView):
    template_name = "student_onboarding.html"

class InstructorOnboardingView(TemplateView):
    template_name = "instructor_onboarding.html"
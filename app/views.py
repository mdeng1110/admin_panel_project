import requests
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from .forms import StudentForm
# Create your views here.
class WelcomeView(TemplateView):
    template_name = "home.html"

class StudentView(TemplateView):
    template_name = "students.html"

class InstructorView(TemplateView):
    template_name = "instructors.html"

class StudentOnboardingView(FormView):
    template_name = "student_onboarding.html"
    form_class = StudentForm
    success_url = "/app/"
    def form_valid(self, form):
        print("something")
        url = "http://localhost:8000/api/instructors/add"
        # form = StudentForm()
        payload = {
            "name": form.cleaned_data["name"],
            "email": form.cleaned_data["email"]
        }
        response = requests.post(url, data=payload)
        print(response.text)
        return super().form_valid(form)
        # return render(request, 'student_onboarding.html', {'form': form})
class InstructorOnboardingView(TemplateView):
    template_name = "instructor_onboarding.html"
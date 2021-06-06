import json
import requests
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm
# Create your views here.
class WelcomeView(TemplateView):
    template_name = "home.html"

class InstructorView(TemplateView):
    template_name = "instructors.html"

class LoginView(TemplateView):
    template_name = "login.html"
    form_class = LoginForm

class SignupView(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = "/app/"
    def form_valid(self, form):
        print("something")
        url = "http://localhost:8000/api/instructors/add"
        password = make_password(form.cleaned_data["password"])
        payload = json.dumps({
            "username": form.cleaned_data["username"],
            "password": form.cleaned_data["password"],
            "name": form.cleaned_data["name"],
            "email": form.cleaned_data["email"]
        })
        response = requests.post(url, data=payload)
        print(response.text)
        return super().form_valid(form)
        # return render(request, 'student_onboarding.html', {'form': form})

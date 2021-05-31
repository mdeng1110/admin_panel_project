from django.urls import include, path
from app import views


urlpatterns = [
    path('', views.WelcomeView.as_view(), name="home"),
    path('student-onboarding/', views.StudentOnboardingView.as_view(), name="student-onboarding"),
    path('instructor-onboarding/', views.InstructorOnboardingView.as_view(), name="instructor-onboarding")
]
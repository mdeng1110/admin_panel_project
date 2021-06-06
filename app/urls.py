from django.urls import include, path
from app import views


urlpatterns = [
    path('', views.WelcomeView.as_view(), name="home"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
]
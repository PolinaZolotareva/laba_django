from django.urls import path
from django.views.generic import ListView, DetailView
from main.models import Schedule
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', ListView.as_view(queryset=Schedule.objects.all(), template_name="main/home.html")),
    path('login/', authViews.LoginView.as_view(template_name="main/login.html"), name="login"),
    path('exit/', authViews.LogoutView.as_view(template_name="main/exit.html"), name="exit"),
    path('registration/', views.registration, name="registration")
]

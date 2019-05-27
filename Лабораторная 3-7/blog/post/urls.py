from django.urls import path
from django.conf.urls import url
from post.models import Post
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.articles, name="articles"),
    path('login/', authViews.LoginView.as_view(template_name="post/login.html"), name="login"),
    path('exit/', authViews.LogoutView.as_view(template_name="post/exit.html"), name="exit"),
    path('registration/', views.registration, name="registration"),
    path('edit/', views.edit, name="edit")
]
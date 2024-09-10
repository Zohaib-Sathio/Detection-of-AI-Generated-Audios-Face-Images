from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path('detect_ai/', views.detect_ai, name='detect_ai'),
    path("articles/", views.articles, name='articles'),
]

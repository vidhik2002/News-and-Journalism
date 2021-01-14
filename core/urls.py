from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('push/', views.myAPI.as_view()),
]

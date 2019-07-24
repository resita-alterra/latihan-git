
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mentee/', views.mentee, name='mentee'),
    path('mentor/', views.mentor),
]
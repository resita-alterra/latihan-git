from django.urls import path, include
from . import views

urlpatterns = [
    path('/mentor', views.mentor),
]
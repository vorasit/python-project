from django.contrib import admin
from django.urls import path
from .views import panel

urlpatterns = [
    path('',panel,name="panel"),
]
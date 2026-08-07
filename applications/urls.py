from django.contrib import admin
from django.urls import path
from .views import jobApllication, Jobapllications


urlpatterns = [
    path("applications/", jobApllication.as_view(), name='jobApllication'),
    path("applications/<int:pk>", Jobapllications.as_view(), name='jobApllication'),
]

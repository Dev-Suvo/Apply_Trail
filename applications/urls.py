from django.contrib import admin
from django.urls import path
from .views import application_list, application_updation


urlpatterns = [
    path("applications/", application_list, name='application_list'),
    path("applications/<int:pk>", application_updation, name='application_updation'),

]

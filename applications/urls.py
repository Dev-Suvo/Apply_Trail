from django.contrib import admin
from django.urls import path
from .views import JobApplication

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'applications',JobApplication, basename='apllications')


urlpatterns = [
    
]

urlpatterns += router.urls

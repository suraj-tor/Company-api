from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(f"companies", CompanyViewsets)
router.register(f"employees", EmployeesViewsets)

urlpatterns = [
    path("", include(router.urls))
]

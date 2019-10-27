from django.urls import path
from .views import locations, shifts

urlpatterns = [
    path('locations', locations),
    path('shifts', shifts)
]

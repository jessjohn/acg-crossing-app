from django.urls import path
from .views import locations_list

urlpatterns = [
    path('', locations_list),
]

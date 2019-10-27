from django.urls import path
from .views import user_shifts, check_in
urlpatterns = [
    path('user-shifts', user_shifts),
    path('check-in', check_in)
]

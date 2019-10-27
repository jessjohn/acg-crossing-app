from django.urls import include, path
from rest_framework.authtoken import views as rf_views
from . import views

urlpatterns = [
    path('users', views.UserListView.as_view()),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('auth/', include('rest_auth.urls'))
]
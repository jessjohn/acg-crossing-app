from django.urls import path, include
from ..apis.location_create import LocationCreateApi
from ..apis.location_delete import LocationDeleteApi
from ..apis.location_list import LocationListAPI
from ..apis.location_detail import LocationDetailAPI
from ..apis.location_update import LocationUpdateAPI

location_patterns = [
    path('', LocationListAPI.as_view(), name='list'),
    path('<int:location_id>/', LocationDetailAPI.as_view(), name='detail'),
    path('create/', LocationCreateApi.as_view(), name='create'),
    path('<int:location_id>/update/', LocationUpdateAPI.as_view(), name='update'),
    path('<int:location_id>/', LocationDeleteApi.as_view(), name='delete'),
]
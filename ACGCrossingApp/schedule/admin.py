from django.contrib import admin
from .models import *

from .models import Location, Shift

admin.site.register(Shift)
admin.site.register(Location)

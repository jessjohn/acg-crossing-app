from django.contrib import admin
from .models import *

<<<<<<< HEAD
# Register your models here.
admin.site.register(Location)
admin.site.register(Shift)
=======
from .models import Location, Shift

admin.site.register(Shift)
admin.site.register(Location)
>>>>>>> 516d50934a6bd6827d664e78bde878d4b7512cab

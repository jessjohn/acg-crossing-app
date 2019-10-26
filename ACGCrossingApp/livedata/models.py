from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class UserShift(models.Model):
    shift = models.ForeignKey() #to do later
    shift_user = models.ForeignKey(
        get_user_model(),
    )
    checked_in = models.BooleanField()
    date = models.DateField()

    
from django.db import models
from django.contrib.auth import get_user_model

from schedule.models import Shift

class UserShift(models.Model):

    shift = models.ForeignKey(
        Shift,
        on_delete=models.PROTECT
    )
    
    shift_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    
    checked_in = models.BooleanField()

    date = models.DateField()

    
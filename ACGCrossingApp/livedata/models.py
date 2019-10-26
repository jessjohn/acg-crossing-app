from django.db import models
from django.contrib.auth import get_user_model

from schedule.models import Shift

class UserShift(models.Model):
<<<<<<< HEAD

    shift = models.ForeignKey(
        Shift,
        on_delete=models.PROTECT
    )
    
    shift_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    
=======
   # shift = models.ForeignKey() #to do later
   # shift_user = models.ForeignKey(
      #  get_user_model(),
    #)
>>>>>>> fbb9da8f524a880d900cc20e27b13c36f4229389
    checked_in = models.BooleanField()

    date = models.DateField()

    
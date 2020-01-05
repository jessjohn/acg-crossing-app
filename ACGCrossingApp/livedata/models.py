from django.db import models
from django.contrib.auth import get_user_model

from schedule.models import Shift

class UserShift(models.Model):

    CHECKED_IN = 'CI'
    DECLINED = 'DE'
    AWAITING_RESPONSE = 'AR' #maybe rename to standby
    #'ABSENT' STATE? We'll track state server side, too hard to compose custom json return objects
    SHIFT_STATUS = [
        (CHECKED_IN, 'Checked In'),
        (DECLINED, 'Declined'),
        (AWAITING_RESPONSE, 'Awaiting Response'),
    ]

    shift = models.ForeignKey(
        Shift,
        on_delete=models.PROTECT
    )
    
    shift_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    
    checked_in = models.CharField(
        max_length=2,
        choices=SHIFT_STATUS,
        default=AWAITING_RESPONSE,
    )

    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

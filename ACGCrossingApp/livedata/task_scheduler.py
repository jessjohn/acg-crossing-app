from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import json

from .models import UserShift
from .serializers import UserShiftReadSerializer
from .models import UserShift

def fetch_today_shifts():
    qs = UserShift.objects.all()
    serializer = UserShiftReadSerializer(qs, many=True)
    print(json.dumps(serializer.data))

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(fetch_today_shifts, 'interval', seconds=3)

    scheduler.start()
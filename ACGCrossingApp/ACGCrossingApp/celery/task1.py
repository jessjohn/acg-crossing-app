from celery.decorators import task
from channels.layers import get channel_layer
from asgiref.sync import async_to_sync

channel_layer=get_channel_layer()


@periodic_task(
    run_every=(crontab(hours='*/12')),
    name="task",
    ignore_result=True
)
def task():
    async_to_sync(channel_layer.group_send)("shift_change", {"type": "HELLO MAMA"})
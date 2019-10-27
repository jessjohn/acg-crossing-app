from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from .models import UserShift
from .serializers import UserShiftReadSerializer

class LiveDataConsumer(WebsocketConsumer):
    """
    Websocket connection to send real-time data to admin
    browser app
    """
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("events", self.channel_name)
        users_shift = UserShift.objects.all() #need to filter
        serializer = UserShiftReadSerializer(users_shift, many=True)
        self.send(json.dumps(serializer.data))
        # self.send(json.dumps(
        #     {
        #         'location': 'location_id',
        #         'status_update': 'new_status'
        #     }
        # ))


    def disconnect(self, close_code):
        pass

    """
    Events group msg formatting:
    {
        "type": "shift.event", //name is significant
        "user_shift_id": user_shift_id,
        "event_message": event_message
    }
    """
    def shift_event(self, event):
        """
        Called when a message has been received in 'events' Channels group
        """
        self.send(
            {
                "user_shift_id": "user_shift_id",
                "updated_status": "new_status"
            }
        )


    # def receive(self, text_data):
    #     """
    #     Listen for scheduled start + end shift events and send to ws client
    #     """
        
    #     # text_data_json = json.loads(text_data)
    #     # message = text_data_json['message']

    #     # self.send(text_data=json.dumps({
    #     #     'message': message
    #     # }))
    #     self.send(text_data)

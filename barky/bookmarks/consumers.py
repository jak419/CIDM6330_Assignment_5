import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Bookmark
from asgiref.sync import sync_to_async

class BookmarkConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass 

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # When a message is received, handling different events
        if message == "fetch_bookmarks":
            bookmarks = await self.get_bookmarks()
            await self.send(text_data=json.dumps({
                'message': bookmarks
            }))

    @sync_to_async
    def get_bookmarks(self):
        bookmarks = list(Bookmark.objects.all().values())
        return json.dumps(bookmarks)  # Serialize query to JSON

    async def bookmark_notify(self, event):
        # Send a message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['text']
        }))

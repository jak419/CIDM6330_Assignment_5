import pytz
from datetime import datetime
from django.db import transaction
from injector import Injector, inject, Module, provider, singleton
from .models import Bookmark

# class definition for TimeStampProvider 
class TimeStampProvider:
    def get_current_time(self):
        return datetime.now(pytz.UTC)

# class definition for Injector module definition
class AppModule(Module):
    @singleton
    @provider
    def provide_timestamp_provider(self) -> TimeStampProvider:
        return TimeStampProvider()

# BookmarkRepository class definition with dependency injection
class BookmarkRepository:
    @inject
    def __init__(self, timestamp_provider: TimeStampProvider):
        self.timestamp_provider = timestamp_provider

    def get_all_bookmarks(self):
        return Bookmark.objects.all()

    def add_bookmark(self, title, url, notes=''):
        timestamp = self.timestamp_provider.get_current_time()
        return Bookmark.objects.create(title=title, url=url, notes=notes, date_added=timestamp)

    def get_bookmark_by_id(self, id):
        return Bookmark.objects.filter(id=id).first()

    def update_bookmark(self, id, **kwargs):
        Bookmark.objects.filter(id=id).update(**kwargs)

    def delete_bookmark(self, id):
        with transaction.atomic():
            bookmark = self.get_bookmark_by_id(id)
            if bookmark:
                bookmark.delete()


injector = Injector([AppModule()]) #setting up injector
bookmark_repository = injector.get(BookmarkRepository) #setting up bookmark_repository to be used in views.py


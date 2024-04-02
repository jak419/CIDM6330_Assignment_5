from .models import Bookmark

class BookmarkRepository:
    def get_all_bookmarks(self):
        return Bookmark.objects.all()

    def add_bookmark(self, title, url, notes=''):
        return Bookmark.objects.create(title=title, url=url, notes=notes)

    def get_bookmark_by_id(self, id):
        return Bookmark.objects.filter(id=id).first()

    def update_bookmark(self, id, **kwargs):
        Bookmark.objects.filter(id=id).update(**kwargs)

    def delete_bookmark(self, id):
        bookmark = self.get_bookmark_by_id(id)
        if bookmark:
            bookmark.delete()

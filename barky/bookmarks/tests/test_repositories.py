from django.test import TestCase
from bookmarks.models import Bookmark
from bookmarks.repositories import BookmarkRepository

class BookmarkRepositoryTest(TestCase):
    def setUp(self):
        # Creating some sample test data
        self.bookmark1 = Bookmark.objects.create(title="Bookmark 1", url="http://example.com")
        self.bookmark2 = Bookmark.objects.create(title="Bookmark 2", url="http://example.org")

    def test_get_all_bookmarks(self):
        repository = BookmarkRepository()
        bookmarks = repository.get_all_bookmarks()
        self.assertEqual(len(bookmarks), 2)

    def test_add_bookmark(self):
        repository = BookmarkRepository()
        bookmark = repository.add_bookmark("New Bookmark", "http://example.net", "Notes")
        self.assertEqual(bookmark.title, "New Bookmark")
        self.assertEqual(bookmark.url, "http://example.net")
        self.assertEqual(bookmark.notes, "Notes")

    def test_get_bookmark_by_id(self):
        repository = BookmarkRepository()
        bookmark = repository.get_bookmark_by_id(self.bookmark1.id)
        self.assertEqual(bookmark.title, "Bookmark 1")
        self.assertEqual(bookmark.url, "http://example.com")

    def test_update_bookmark(self):
        repository = BookmarkRepository()
        repository.update_bookmark(self.bookmark1.id, title="Updated Bookmark")
        bookmark = Bookmark.objects.get(id=self.bookmark1.id)
        self.assertEqual(bookmark.title, "Updated Bookmark")

    def test_delete_bookmark(self):
        repository = BookmarkRepository()
        repository.delete_bookmark(self.bookmark1.id)
        bookmarks = repository.get_all_bookmarks()
        self.assertEqual(len(bookmarks), 1)
from django.test import TestCase
from django.utils import timezone
from bookmarks.models import Bookmark

class BookmarkModelTest(TestCase):
    def test_bookmark_creation(self):
        bookmark = Bookmark.objects.create(title="Test Bookmark", url="http://example.com", notes="This is a test")
        self.assertEqual(bookmark.title, "Test Bookmark")
        self.assertEqual(bookmark.url, "http://example.com")
        self.assertEqual(bookmark.notes, "This is a test")  # Make sure this matches exactly what you set


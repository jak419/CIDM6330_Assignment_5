from django.test import TestCase, Client
from django.urls import reverse
from bookmarks.models import Bookmark

class BookmarkViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Bookmark.objects.create(title="First Bookmark", url="http://first.com")
        Bookmark.objects.create(title="Second Bookmark", url="http://second.com")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookmarks/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookmark-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookmark-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookmarks/bookmark_list.html')

    #def test_pagination_is_ten(self):
        # If you have pagination
        #response = self.client.get(reverse('bookmark-list'))
        #self.assertTrue('is_paginated' in response.context)
        #self.assertTrue(response.context['is_paginated'] == True)
        #self.assertTrue(len(response.context['bookmark_list']) == 10)

    def test_lists_all_bookmarks(self):
        # Adjust the number according to the pagination settings
        response = self.client.get(reverse('bookmark-list')+'?page=2')
        self.assertTrue(len(response.context['bookmark_list']) == 2)

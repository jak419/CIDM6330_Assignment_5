from django.urls import path
from .views import BookmarkAddView
from .views import BookmarkListView

urlpatterns = [
    path('bookmarks/', BookmarkListView.as_view(), name='bookmark-list'),
    path('add/', BookmarkAddView.as_view(), name='bookmark-add'),
]



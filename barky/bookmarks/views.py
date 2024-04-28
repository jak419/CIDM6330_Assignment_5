from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .repositories import BookmarkRepository
from django.shortcuts import redirect
from django.views import View
from .models import Bookmark
from .repositories import bookmark_repository 

class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'bookmarks/bookmark_list.html'
    paginate_by = 10

    def get_queryset(self):
        #repository = BookmarkRepository()
        #return repository.get_all_bookmarks()
        return bookmark_repository.get_all_bookmarks()


class BookmarkAddView(View):
    def post(self, request, *args, **kwargs):
        #  having title, url, and notes from the request.POST
        title = request.POST.get('title')
        url = request.POST.get('url')
        notes = request.POST.get('notes', '')
        
        #repository = BookmarkRepository()
        #repository.add_bookmark(title, url, notes)
        bookmark_repository.add_bookmark(title, url, notes)

        return redirect('bookmark-list')
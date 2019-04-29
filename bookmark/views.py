#-*-coding:cp949-*-
from django.shortcuts import render,get_object_or_404
from .models import Bookmark
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('q')
        if search:
            object_list = self.model.objects.filter(site_name__icontains=search)
        else:
            object_list = self.model.objects.all()
        return object_list

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

from django.contrib import admin
from .models import Bookmark
# Register your models here.

@admin.register(Bookmark)
class adminbookmark(admin.ModelAdmin):
    list_display = ('site_name','url')

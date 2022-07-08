from django.contrib import admin

# Register your models here.
from .models import NewsArtical, NewspaperTitle, NewsComment

admin.site.register(NewsArtical)
admin.site.register(NewspaperTitle)
admin.site.register(NewsComment)

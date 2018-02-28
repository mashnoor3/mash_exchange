# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin (admin.ModelAdmin):
	class Meta:
		model = Book

admin.site.register(Book, BookAdmin)

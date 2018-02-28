from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse


class Book(models.Model):
    title = models.CharField(max_length=250)
    subject = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='books')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

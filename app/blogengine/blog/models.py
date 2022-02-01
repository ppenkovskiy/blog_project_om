from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absulute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


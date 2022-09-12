from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    active  = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("Blog:article-detail", kwargs={"id":self.id})

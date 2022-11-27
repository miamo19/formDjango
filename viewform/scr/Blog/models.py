from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    active  = models.BooleanField(default=False)
    price   = models.DecimalField(max_digits =15, decimal_places=2, default=99.99 )


    def get_absolute_url(self):
        return reverse("Blog:article-detail", kwargs={"id":self.id})

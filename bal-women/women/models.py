import uuid

from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", default="")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'

    def __str__(self):
        return self.title

# кнопка смотреть на сайте
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",null=True)
    allow_empty = False

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']



from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url cat')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_by_cat', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Url tag')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('post_by_tag', kwargs={'slug': self.slug})

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Url post')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Updated")
    views = models.PositiveIntegerField(default=0, verbose_name='Count of views')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tag = models.ManyToManyField(Tag, related_name='posts')
    is_published = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-create_at']

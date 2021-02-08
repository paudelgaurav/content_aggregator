from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Topic(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    subscriber = models.ManyToManyField(User, related_name='topics',blank=True)


    def __str__(self):
        return self.title

class News(models.Model):
    topic = models.ForeignKey(Topic, related_name='news',on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    url = models.URLField()
    source = models.CharField(max_length=100,default='admin')

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title
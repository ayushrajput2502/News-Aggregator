from django.db import models
from django.contrib.auth.models import User


class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class EHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class SHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class PHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class LHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class ENHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title
    
class Bookmark(models.Model):
    source = models.CharField(max_length=200,null = True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_url = models.URLField()
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bookmark - {self.user.username} - {self.source}"
from django.db import models
from django.conf import settings
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    # likes = models.ManyToManyField(settings.AUTH_USER_MODEL, black = True, related_name='likes', through='Like')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]


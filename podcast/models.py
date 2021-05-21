from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField

User = get_user_model()


class Podcast(models.Model):
    title = models.CharField(max_length=70)
    discription = models.TextField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    # content = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    google = models.URLField(max_length=195, blank=True, null=True)
    youtube = models.URLField(max_length=195, blank=True, null=True)
    spotify = models.URLField(max_length=195, blank=True, null=True)
    apple = models.URLField(max_length=195, blank=True, null=True)
    soundcloud = models.URLField(max_length=195, blank=True, null=True)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

   


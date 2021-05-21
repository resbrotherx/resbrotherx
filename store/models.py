from django.db import models
# from user.models import profile as User
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    image = models.ImageField(default='media/default.jpg')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    discription = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('graphics:graphics_category', args=[self.slug])

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "tag"
        verbose_name_plural = 'tags'

    def get_absolute_url(self):
        return reverse('graphics:list_tags', args=[self.slug])

    def __str__(self):
        return self.name



# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=50)
    # created_on = models.DateField(auto_now=True)
    item_created_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.FloatField(default=1.0)
    image = models.ImageField()
    image_path = models.FileField()
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tags)
    featured = models.BooleanField()
     = models.BooleanField()
    icon = models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return reverse('graphics:graphic_details', kwargs={
            'id': self.id
        })


    def __str__(self):
        return f'{self.title} - {self.user.first_name} - {self.pk}'

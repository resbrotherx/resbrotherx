from django.db import models
# from user.models import profile as User
from django.urls import reverse
# from PIL import Image
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="users",)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=200)
    tag = models.ManyToManyField('Tags')
    slug = models.SlugField(max_length=250, unique=True)
    discription = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('items:list_category', args=[self.slug])

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "tag"
        verbose_name_plural = 'tags'

    def get_absolute_url(self):
        return reverse('items:list_tags', args=[self.slug])

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
        return reverse('items:list_tags', args=[self.slug])

    def __str__(self):
        return self.name


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    # created_on = models.DateField(auto_now=True)
    item_created_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_type = models.CharField(max_length=50, choices=(('1','p'),('0','t')), default='1')
    price = models.FloatField(default=1.0)
    image = models.ImageField()
    image_path = models.FileField()
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tags)
    featured = models.BooleanField()
    
    
    def get_absolute_url(self):
        return reverse('items:item_detail', kwargs={
            'id': self.id
        })



    def __str__(self):
        return f'{self.title} - {self.user.first_name} - {self.pk}'


# nt used yet, use to store multi images for item
class ItemImage(models.Model):
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    created_on = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.item.title} - {self.created_on}'



class picture(models.Model):
    title = models.CharField(max_length=70)
    discription = models.TextField(max_length=135)
    timestamp = models.DateTimeField(auto_now_add=True)
    # content = HTMLField()
    vcount = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    image2 = models.ImageField(blank=True, null=True)
    video_url = models.URLField(max_length=195, blank=True, null=True)
    tag = models.ManyToManyField(Tag)
    featured = models.BooleanField()
    slug = models.SlugField(max_length=70, unique=True)
    likes=models.ManyToManyField(User, related_name="pic_loved", blank=True, null=True)
    dislikes=models.ManyToManyField(User, related_name="pic_disliked", blank=True, null=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('items:pictures_details', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })

    def num_likes(self):
        return self.likes.count()

    def num_dislikes(self):
        return self.dislikes.count()

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()





        
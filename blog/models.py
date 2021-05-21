from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField
from user.models import profile

User = get_user_model()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=70, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absoulte_url(self):
        return reverse('cate', args=[self.title])

    def __str__(self):
        return self.title

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    likes=models.ManyToManyField(User, related_name="loved", blank=True, null=True)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def num_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=70)
    discription = models.TextField(max_length=135)
    timestamp = models.DateTimeField(auto_now_add=True)
    # content = HTMLField()
    count = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    image2 = models.ImageField(blank=True, null=True)
    video_url = models.URLField(max_length=195, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    slug = models.SlugField(max_length=70, unique=True)
    likes=models.ManyToManyField(User, related_name="post_loved", blank=True, null=True)
    dislikes=models.ManyToManyField(User, related_name="post_disliked",blank=True, null=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('items:blog_detail', kwargs={
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





from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="auth",)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=70)
    job_description = models.TextField()
    skill_requirement = models.TextField()
    additional_information = models.TextField()
    how_to_apply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # content = HTMLField()
    country = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    vcount = models.IntegerField(default = 0)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    logo = models.ImageField()
    featured = models.BooleanField()
    slug = models.SlugField(max_length=70, unique=True)
    # likes=models.ManyToManyField(User, related_name="pic_loved", blank=True, null=True)
    # dislikes=models.ManyToManyField(User, related_name="pic_disliked", blank=True, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('items:job_details', kwargs={
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




# Create your models here.
class Studios(models.Model):
    title = models.CharField(max_length=70)
    about = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # content = HTMLField()
    country = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    vcount = models.IntegerField(default = 0)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    banner = models.ImageField()
    logo = models.ImageField()
    website = models.URLField(max_length=195, blank=True, null=True)
    jobs = models.ManyToManyField(Jobs, related_name="jb")
    featured = models.BooleanField()
    slug = models.SlugField(max_length=70, unique=True)
    # likes=models.ManyToManyField(User, related_name="pic_loved", blank=True, null=True)
    # dislikes=models.ManyToManyField(User, related_name="pic_disliked", blank=True, null=True)
    # previous_post = models.ForeignKey(
    #     'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    # next_post = models.ForeignKey(
    #     'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('items:job_details', kwargs={
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



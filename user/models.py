from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# # Create your models here.
# class User(models.Model):

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'



class profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    gender = models.TextField(choices=(('1', 'm'), ('0', 'f')), default='0')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    city = models.CharField(default='New york', max_length=100)
    country = models.CharField(default='USA', max_length=100)
    # first_name = models.CharField(max_length=50)
    # other_name = models.CharField(max_length=50, null=True, blank=True)
    # last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(profile, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return str(self.user)



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='profile_pics', default='default.jpg')

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         super(Profile, self).save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)







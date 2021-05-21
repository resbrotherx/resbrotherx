from django.db import models
from user.models import profile as User
from items.models import Item

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE)
    price = models.FloatField()
    status = models.CharField(max_length=10,choices=(('1','completed'),('0','pending'), ('-1','cancelled')), default='0')
    created_on = models.DateField(auto_now=True)
    finalized_on = models.DateField(null=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.item.title} - {self.created_on}'


class Download(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order,on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.item.title} - {self.created_on}'
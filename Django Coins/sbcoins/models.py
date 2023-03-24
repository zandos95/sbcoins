from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    ycoin=models.DateField(null=True)
    text=models.TextField()
    cprice=models.IntegerField(default=0)
    img=models.ImageField(blank=True,null=True)
    created_date=models.DateTimeField(default=timezone.now)
    

# Create your models here.

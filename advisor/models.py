from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class AdvisorModel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    advname = models.CharField(max_length=20)
    image = models.ImageField(upload_to = "file",null=True)
    booking_id = models.IntegerField(default = True,null=False,)
    booking_date = models.DateTimeField(auto_now=timezone.now)
    def __str__(self):
        return self.advname

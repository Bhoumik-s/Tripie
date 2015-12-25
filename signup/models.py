from django.db import models
from django.utils import timezone

# Create your models here.
class User_db(models.Model):
    deviceId = models.CharField(max_length=16)
    mobile = models.CharField('Mobile',max_length=13)
    created = models.DateTimeField(default=timezone.now)
    accessToken = models.CharField(max_length=16)
    
    def __str__(self):
        return self.mobile



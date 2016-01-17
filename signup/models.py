from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    DeviceId = models.CharField(max_length=16)
    Mobile = models.CharField('Mobile',max_length=13)
    Created = models.DateTimeField(default=timezone.now)
    AccessToken = models.CharField(max_length=16)
    Name = models.CharField(max_length = 100)
    EmailId = models.EmailField()
    FbId = models.CharField(max_length = 25)
    GoogleId = models.CharField(max_length = 25)
    EconomyStatus = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.EmailField




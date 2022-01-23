from django.db import models


# Create your models here.
class KB(models.Model):
    id = models.AutoField(primary_key=True)
    kbid = models.CharField(max_length=15)
    cveid = models.CharField(max_length=50)
    exp = models.CharField(max_length=100)

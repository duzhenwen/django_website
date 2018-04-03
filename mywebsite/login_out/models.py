from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class user_infor(models.Model):
    username=models.CharField(max_length=20,blank=False)
    telephone=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=20,blank=False)
    password=models.CharField(max_length=20,blank=False)
    def __str__(self):
        return self.username

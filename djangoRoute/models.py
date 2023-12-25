from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=30, unique=True)  # name varchar(30)
    age = models.IntegerField(default=18)                # age int default 18
    is_deleted = models.BooleanField(default=False)

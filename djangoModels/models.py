from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=30, unique=True)  # name varchar(30)
    age = models.IntegerField(default=18)                # age int default 18
    is_deleted = models.BooleanField(default=False)


class PersonModel(models.Model):
    # Create customized primary key instead of relying on default
    uid = models.AutoField(auto_created=True, primary_key=True)

    # db_index is set to true to make the column index
    name = models.CharField(max_length=30, unique=True, db_index=True)  # name varchar(30)

    # Use default to set the age
    age = models.IntegerField(default=18)                # age int default 18

    # Use text field (make it optional)
    self_intro = models.TextField(null=True, blank=True)

    # Use decimals (limit the number of decimal digits to 2)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=150.00)

    is_deleted = models.BooleanField(default=False)



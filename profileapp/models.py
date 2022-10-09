from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)



class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User,blank=False, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    location = models.CharField(max_length=120, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    # zip_code = models.CharField(max_length=5, validators=[validators.MinLengthValidator(5)], blank=False)

        
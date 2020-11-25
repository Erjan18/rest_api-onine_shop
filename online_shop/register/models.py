from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class Account(AbstractBaseUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

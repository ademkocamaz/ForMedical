from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = None

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
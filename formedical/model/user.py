from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .nurse import *


class UserManager(models.Manager):
    use_in_migrations=True

    def get_by_natural_key(self, kullaniciadi):
        return self.get(**{self.model.USERNAME_FIELD: kullaniciadi})



class User(AbstractBaseUser, Nurse, PermissionsMixin):
    
    password = Nurse.sifre 
    is_active = True
    is_superuser = True     
    
    objects = UserManager()

    USERNAME_FIELD = "kullaniciadi"
    REQUIRED_FIELDS = []

    # def get_full_name(self):
    #     full_name = self.kullaniciadi
    #     return full_name.strip()

    # def get_short_name(self):
    #     return self.kullanici
    
    # class Meta:
    #     verbose_name = 'Kullanıcı'
    #     verbose_name_plural = 'Kullanıcılar'
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserManager(models.Manager):
    use_in_migrations=True
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

class User(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(db_column='ID', primary_key=True)
    username = models.CharField(db_column='KULLANICIADI', max_length=50, verbose_name='Kullanıcı Adı', unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='SIFRE', max_length=10, blank=True, null=True, verbose_name='Şifre')  # Field name made lowercase.
    user = models.CharField(db_column='KULLANICI', max_length=5, blank=True, null=True, verbose_name='Kullanıcı')  # Field name made lowercase.
    group = models.CharField(db_column='GRUP', max_length=30, blank=True, null=True, verbose_name='Grup')  # Field name made lowercase.
    is_inactive=models.BooleanField(db_column='PASIF', default=False,verbose_name='Pasif ?')
    is_admin = True
    is_superuser = models.BooleanField(db_column='SUPER', default=False)
    last_login=None
    objects=UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def set_password(self, raw_password):
        self.password = raw_password
        

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        return True

    def has_usable_password(self):
        """
        Return False if set_unusable_password() has been called for this user.
        """
        return True

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_KULLAN'
        verbose_name='Kullanıcı'
        verbose_name_plural='Kullanıcılar'
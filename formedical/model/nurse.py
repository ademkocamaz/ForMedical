# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Nurse(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kullaniciadi = models.CharField(db_column='KULLANICIADI', max_length=50, verbose_name='Kullanıcı Adı')  # Field name made lowercase.
    sifre = models.CharField(db_column='SIFRE', max_length=10, blank=True, null=True, verbose_name='Şifre')  # Field name made lowercase.
    kullanici = models.CharField(db_column='KULLANICI', max_length=5, blank=True, null=True, verbose_name='Kullanıcı')  # Field name made lowercase.
    grup = models.CharField(db_column='GRUP', max_length=30, blank=True, null=True, verbose_name='Grup')  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_KULLAN'
        verbose_name='Hemşire'
        verbose_name_plural='Hemşireler'
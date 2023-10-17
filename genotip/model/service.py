# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from genotip.model.visit import Visit

class ServiceDefinition(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ad = models.CharField(db_column='AD', max_length=50, verbose_name='Servis Bilgisi')  # Field name made lowercase.
    aktif = models.SmallIntegerField(db_column='AKTIF', verbose_name='Aktif ?')  # Field name made lowercase.
    toplam_yatak_sayi = models.SmallIntegerField(db_column='TOPLAM_YATAK_SAYI', blank=True, null=True, verbose_name='Toplam Yatak Sayısı')  # Field name made lowercase.
    toplam_kuvoz_sayi = models.SmallIntegerField(db_column='TOPLAM_KUVOZ_SAYI', blank=True, null=True, verbose_name='Toplam Küvöz Sayısı')  # Field name made lowercase.
    toplam_vent_sayi = models.SmallIntegerField(db_column='TOPLAM_VENT_SAYI', blank=True, null=True, verbose_name='Toplam Vent Sayısı')  # Field name made lowercase.

    def __str__(self):
        return self.ad

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_SERVISLER'
        verbose_name='Servis Tanımı'
        verbose_name_plural='Servis Tanımları'


class Service(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    visit = models.ForeignKey(
        Visit,
        on_delete=models.DO_NOTHING,
        db_column='GELISID',
        to_field='id', 
        blank=True, 
        null=True,
        db_constraint=False,
        verbose_name='Geliş Bilgileri'
    )  # Field name made lowercase.
    dosyano = models.CharField(db_column='DOSYANO', max_length=15, verbose_name='Dosya Numarası')  # Field name made lowercase.
    gelisno = models.SmallIntegerField(db_column='GELISNO', verbose_name='Geliş No')  # Field name made lowercase.
    servis = models.CharField(db_column='SERVIS', verbose_name='Servis', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doktor = models.CharField(db_column='DOKTOR', verbose_name='Doktor', max_length=25, blank=True, null=True)  # Field name made lowercase.
    oda = models.CharField(db_column='ODA', verbose_name='Oda', max_length=10, blank=True, null=True)  # Field name made lowercase.
    yatak = models.CharField(db_column='YATAK', verbose_name='Yatak',max_length=5, blank=True, null=True)  # Field name made lowercase.
    hemsire = models.CharField(db_column='HEMSIRE', verbose_name='Hemşire', max_length=25, blank=True, null=True)  # Field name made lowercase.
    giristarih = models.DateTimeField(db_column='GIRISTARIH', verbose_name='Giriş Tarihi', blank=True, null=True)  # Field name made lowercase.
    cikistarih = models.DateTimeField(db_column='CIKISTARIH', verbose_name='Çıkış Tarihi', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return 'Dosya No: ' + str(self.dosyano) +' Oda: ' + str(self.oda)+' Yatak: ' + str(self.yatak) # + ' Giriş: '+ str(self.giristarih.strftime('%d.%m.%Y') if self.giristarih.strftime('%d.%m.%Y') is None else 'Girilmemiş')

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_SERVIS'
        verbose_name='Servis'
        verbose_name_plural='Servisler'

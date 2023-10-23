# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from genotip._model.patient import Patient

class Visit(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    patient = models.ForeignKey(
        Patient, 
        db_column='KIMLIKID',
        to_field='id', 
        on_delete=models.DO_NOTHING, 
        verbose_name='Hasta Bilgileri', 
        db_constraint=False,
    )
    dosyano = models.CharField(db_column='DOSYANO', max_length=15, unique=True, verbose_name='Dosya Numarası')  # Field name made lowercase.
    gelisno = models.SmallIntegerField(db_column='GELISNO', verbose_name='Geliş No')  # Field name made lowercase.
    giristarih = models.DateTimeField(db_column='GIRISTARIH', blank=True, null=True, verbose_name='Giriş Tarihi')  # Field name made lowercase.
    cikistarih = models.DateTimeField(db_column='CIKISTARIH', blank=True, null=True, verbose_name='Çıkış Tarihi')  # Field name made lowercase.
    yatgunsay = models.SmallIntegerField(db_column='YATGUNSAY', blank=True, null=True, verbose_name='Yattığı Gün Sayısı')  # Field name made lowercase.
    tedavi = models.CharField(db_column='TEDAVI', max_length=15, blank=True, null=True, verbose_name='Tedavi')  # Field name made lowercase.
    kurum = models.CharField(db_column='KURUM', max_length=200, blank=True, null=True, verbose_name='Kurum')  # Field name made lowercase.
    poliklinik = models.CharField(db_column='POLIKLINIK', max_length=20, blank=True, null=True, verbose_name='Poliklinik')  # Field name made lowercase.
    doktor = models.CharField(db_column='DOKTOR', max_length=50, blank=True, null=True, verbose_name='Doktor')  # Field name made lowercase.
    protokolno = models.CharField(db_column='PROTOKOLNO', max_length=10, blank=True, null=True, verbose_name='Protokol')  # Field name made lowercase.
    icdkodu = models.CharField(db_column='ICDKODU', max_length=100, blank=True, null=True,verbose_name='ICD Kodu')  # Field name made lowercase.
    icdadi = models.CharField(db_column='ICDADI', max_length=200, blank=True, null=True, verbose_name='ICD Adı')  # Field name made lowercase.
    # sonuc = models.CharField(db_column='SONUC', max_length=4000, blank=True, null=True, verbose_name='Sonuç')  # Field name made lowercase.

    def __str__(self) -> str:
        return 'Dosya No: '+ self.dosyano + ' - Geliş No: ' + str(self.gelisno)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_GELISLER'
        verbose_name='Geliş'
        verbose_name_plural='Gelişler'

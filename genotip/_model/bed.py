# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from genotip._model.service import ServiceDefinition, Service

class Bed(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    servis_adi = models.CharField(db_column='SERVIS_ADI', max_length=50, verbose_name='Servis Bilgisi')  # Field name made lowercase.
    oda = models.CharField(db_column='ODA', max_length=15, verbose_name='Oda Bilgisi')  # Field name made lowercase.
    yatak = models.CharField(db_column='YATAK', max_length=5, verbose_name='Yatak No')  # Field name made lowercase.
    
    service_definition = models.ForeignKey(
        to=ServiceDefinition,
        on_delete=models.DO_NOTHING,
        verbose_name='Servis Tanımı',
        to_field='id', 
        db_column='SERVISTANIMID', 
        db_constraint=False,
    )
    durum = models.CharField(db_column='DURUM', max_length=10, blank=True, null=True, verbose_name='Durum')  # Field name made lowercase.
    
    service = models.ForeignKey(
        to=Service, 
        on_delete=models.DO_NOTHING,
        to_field='id', 
        db_column='SERVISID',
        db_constraint=False
    )


    # servis112kodu = models.CharField(db_column='SERVIS112KODU', max_length=30, blank=True, null=True, verbose_name='Servis 112 Kodu')  # Field name made lowercase.
    def __str__(self):
        return "Oda:" + self.oda + " Yatak No:" + self.yatak + " Durum:" + self.durum
    
    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_YATAKDURUM'
        verbose_name='Yatak'
        verbose_name_plural='Yataklar'

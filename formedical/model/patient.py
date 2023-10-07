from django.db import models

class Patient(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dosyano = models.CharField(db_column='DOSYANO', max_length=15, verbose_name='Dosya Numarası')  # Field name made lowercase.
    ad = models.CharField(db_column='AD', max_length=20, blank=True, null=True, verbose_name='Adı')  # Field name made lowercase.
    soyad = models.CharField(db_column='SOYAD', max_length=20, blank=True, null=True, verbose_name='Soyadı')  # Field name made lowercase.
    dogumtarih = models.DateTimeField(db_column='DOGUMTARIH', blank=True, null=True, verbose_name='Doğum Tarihi')  # Field name made lowercase.
    cinsiyet = models.CharField(db_column='CINSIYET', max_length=5, blank=True, null=True, verbose_name='Cinsiyeti')  # Field name made lowercase.
    vatandaslikno = models.CharField(db_column='VATANDASLIKNO', max_length=50, blank=True, null=True, verbose_name='Vatandaşlık Numarası')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.dosyano + ' - ' + self.ad + ' ' + self.soyad
    
    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_KIMLIK'
        verbose_name='Hasta Kaydı'
        verbose_name_plural='Hasta Kayıtları'
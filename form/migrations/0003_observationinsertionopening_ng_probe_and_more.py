# Generated by Django 4.2.7 on 2023-12-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_observationtracking_implementation'),
    ]

    operations = [
        migrations.AddField(
            model_name='observationinsertionopening',
            name='ng_probe',
            field=models.DateTimeField(blank=True, null=True, verbose_name='NG Sonda - Tarih/Saat'),
        ),
        migrations.AlterField(
            model_name='observationinsertionopening',
            name='urinary_catheter',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Üriner Kateter - Tarih/Saat'),
        ),
    ]

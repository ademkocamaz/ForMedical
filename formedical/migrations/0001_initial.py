# Generated by Django 4.2.6 on 2023-10-08 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('dosyano', models.CharField(db_column='DOSYANO', max_length=15, unique=True, verbose_name='Dosya Numarası')),
                ('ad', models.CharField(blank=True, db_column='AD', max_length=20, null=True, verbose_name='Adı')),
                ('soyad', models.CharField(blank=True, db_column='SOYAD', max_length=20, null=True, verbose_name='Soyadı')),
                ('dogumtarih', models.DateTimeField(blank=True, db_column='DOGUMTARIH', null=True, verbose_name='Doğum Tarihi')),
                ('cinsiyet', models.CharField(blank=True, db_column='CINSIYET', max_length=5, null=True, verbose_name='Cinsiyeti')),
                ('vatandaslikno', models.CharField(blank=True, db_column='VATANDASLIKNO', max_length=50, null=True, verbose_name='Vatandaşlık Numarası')),
            ],
            options={
                'verbose_name': 'Hasta Kaydı',
                'verbose_name_plural': 'Hasta Kayıtları',
                'db_table': 'VIEW_GENOTIP_KIMLIK',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosyano', models.CharField(db_column='DOSYANO', max_length=15, unique=True)),
                ('gelisno', models.SmallIntegerField(db_column='GELISNO')),
                ('giristarih', models.DateTimeField(blank=True, db_column='GIRISTARIH', null=True)),
                ('cikistarih', models.DateTimeField(blank=True, db_column='CIKISTARIH', null=True)),
                ('yatgunsay', models.SmallIntegerField(blank=True, db_column='YATGUNSAY', null=True)),
                ('tedavi', models.CharField(blank=True, db_column='TEDAVI', max_length=15, null=True)),
                ('kurum', models.CharField(blank=True, db_column='KURUM', max_length=200, null=True)),
                ('poliklinik', models.CharField(blank=True, db_column='POLIKLINIK', max_length=20, null=True)),
                ('doktorkod', models.CharField(blank=True, db_column='DOKTORKOD', max_length=3, null=True)),
                ('doktor', models.CharField(blank=True, db_column='DOKTOR', max_length=50, null=True)),
                ('protokolno', models.CharField(blank=True, db_column='PROTOKOLNO', max_length=10, null=True)),
                ('icdkodu', models.CharField(blank=True, db_column='ICDKODU', max_length=100, null=True)),
                ('icdadi', models.CharField(blank=True, db_column='ICDADI', max_length=200, null=True)),
                ('sonuc', models.CharField(blank=True, db_column='SONUC', max_length=4000, null=True)),
            ],
            options={
                'verbose_name': 'Geliş',
                'verbose_name_plural': 'Gelişler',
                'db_table': 'VIEW_GENOTIP_GELISLER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('numericalPainScale', models.PositiveSmallIntegerField(choices=[(0, '0. Ağrı Yok'), (1, '1.'), (2, '2.'), (3, '3.'), (4, '4.'), (5, '5. Orta Şiddetli Ağrı'), (6, '6.'), (7, '7.'), (8, '8.'), (9, '9.'), (10, '10. Şiddetli Ağrı')], default=0, verbose_name='Numerik Ağrı Skalası (0-10)')),
                ('wongBakerFacesPainScale', models.PositiveSmallIntegerField(choices=[(0, '0. Ağrı Yok'), (2, '2.'), (4, '4. Orta Şiddetli Ağrı'), (6, '6. Orta Şiddetli Ağrı'), (8, '8.'), (10, '10. Şiddetli Ağrı')], default=0, verbose_name='Yüz Skalası (0-10)')),
                ('behavioralFaceExpressionPainScale', models.PositiveSmallIntegerField(choices=[(0, '0. Ağrı İfadesi Yok / Gülümsüyor'), (1, '1. Nadir Yüz Buruşturma, Çatık Kaş İlgisiz'), (2, '2. Sık Sık Çenesini ve Dişlerini Sıkıyor')], default=0, verbose_name='Davranışsal Ağrı Skalası - Yüz İfadesi (0-2)')),
                ('behavioralLegMovementsPainScale', models.PositiveSmallIntegerField(choices=[(0, '0. Normal / Rahat Pozisyonda'), (1, '1. Huzursuz'), (2, '2. Tekmeleme / Bacakları Çekme')], default=0, verbose_name='Davranışsal Ağrı Skalası - Bacak Hareketleri (0-2)')),
                ('behavioralActivityPainScale', models.PositiveSmallIntegerField(choices=[(0, '0. Sakin Yatış / Rahat Pozisyon'), (1, '1. Gergin / Kıvranıyor'), (2, '2. Hassas / Gergin')], default=0, verbose_name='Davranışsal Ağrı Skalası - Aktivite (0-2)')),
                ('behavioralCryPainScale', models.PositiveSmallIntegerField(choices=[(0, '0. Ağlama Yok'), (1, '1. Arasıra İnleme / Ağlama'), (2, '2. Sürekli Ağlama / Bağırma')], default=0, verbose_name='Davranışsal Ağrı Skalası - Ağlama (0-2)')),
                ('behavioralComfortedPainScale', models.PositiveSmallIntegerField(choices=[(0, '0. Memnun / Rahat'), (1, '1. Arasıra Çevreden Rahatsız'), (2, '2. Avutulması Zor')], default=0, verbose_name='Davranışsal Ağrı Skalası - Avutulma (0-2)')),
                ('patient', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='formedical.patient', verbose_name='Hasta Bilgileri')),
            ],
            options={
                'verbose_name': 'Ağrı Formu',
                'verbose_name_plural': 'Ağrı Formları',
            },
        ),
        migrations.CreateModel(
            name='PainTargetedLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Hedeflenen Ağrı Düzeyi (Hasta İle İşbirliği Halinde Hemşire Tarafından)')),
                ('date', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formedical.pain', verbose_name='Ağrı Formu')),
            ],
            options={
                'verbose_name': 'Hedeflenen Ağrı Düzeyi (Hasta İle İşbirliği Halinde Hemşire Tarafından)',
                'verbose_name_plural': 'Hedeflenen Ağrı Düzeyi Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='PainSeverity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Ağrının Şiddeti (Skalalardan Uygun Olan Kullanılır)')),
                ('date', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formedical.pain', verbose_name='Ağrı Formu')),
            ],
            options={
                'verbose_name': 'Ağrının Şiddeti (Skalalardan Uygun Olan Kullanılır)',
                'verbose_name_plural': 'Ağrı Şiddeti Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='PainScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Ağrı Skalası (Numerik Davransal Yüz)')),
                ('date', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formedical.pain', verbose_name='Ağrı Formu')),
            ],
            options={
                'verbose_name': 'Ağrı Skalası (Numerik Davransal Yüz)',
                'verbose_name_plural': 'Ağrı Skala Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='PainPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Ağrının Yeri (Hastanın Kendi İfadesi / Hemşirenin Gözlemi)')),
                ('date', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formedical.pain', verbose_name='Ağrı Formu')),
            ],
            options={
                'verbose_name': 'Ağrının Yeri (Hastanın Kendi İfadesi / Hemşirenin Gözlemi)',
                'verbose_name_plural': 'Ağrı Yeri Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='PainNature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Ağrının Niteliği (Hastanın Kendi İfadesi İle)')),
                ('date', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formedical.pain', verbose_name='Ağrı Formu')),
            ],
            options={
                'verbose_name': 'Ağrının Niteliği (Hastanın Kendi İfadesi İle)',
                'verbose_name_plural': 'Ağrı Niteliği Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='PainFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Ağrının Sıklığı (Hastanın Kendi İfadesi İle)')),
                ('date', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formedical.pain', verbose_name='Ağrı Formu')),
            ],
            options={
                'verbose_name': 'Ağrının Sıklığı (Hastanın Kendi İfadesi İle)',
                'verbose_name_plural': 'Ağrı Sıklığı Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='PainFactorAffecting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Ağrıyı Etkileyen Faktörler (Hastanın Kendi İfadesi / Hemşirenin Gözlemi)')),
                ('date', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('pain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formedical.pain', verbose_name='Ağrı Formu')),
            ],
            options={
                'verbose_name': 'Ağrıyı Etkileyen Faktörler (Hastanın Kendi İfadesi / Hemşirenin Gözlemi)',
                'verbose_name_plural': 'Ağrı Faktör Kayıtları',
            },
        ),
    ]

from django.db import models
from formedical.model.service import Service
from django.conf import settings

class Pain(models.Model):
    # patient = models.ForeignKey(
    #     Gelisler,
    #     on_delete=models.DO_NOTHING,
    #     verbose_name='Dosya Numarası'
    # )
    service = models.ForeignKey(
        Service,
        on_delete=models.DO_NOTHING,
        verbose_name='Servis Bilgileri',
        db_constraint=False,
        # editable=False
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.DO_NOTHING, 
        verbose_name='Kullanıcı',
        db_constraint=False,
        # default=
    )
    # region Scale

    # region numericalPainScale

    numericalPainScaleChoices = [
        (0, '0. Ağrı Yok'),
        (1, '1.'),
        (2, '2.'),
        (3, '3.'),
        (4, '4.'),
        (5, '5. Orta Şiddetli Ağrı'),
        (6, '6.'),
        (7, '7.'),
        (8, '8.'),
        (9, '9.'),
        (10, '10. Şiddetli Ağrı')
    ]

    numericalPainScale = models.PositiveSmallIntegerField(
        verbose_name='Numerik Ağrı Skalası (0-10)',
        choices=numericalPainScaleChoices,
        default=0
    )

    # endregion

    # region wongBakerFacesPainScale

    wongBakerFacesPainScaleChoices = [
        (0, '0. Ağrı Yok'),
        (2, '2.'),
        (4, '4. Orta Şiddetli Ağrı'),
        (6, '6. Orta Şiddetli Ağrı'),
        (8, '8.'),
        (10, '10. Şiddetli Ağrı')
    ]

    wongBakerFacesPainScale = models.PositiveSmallIntegerField(
        verbose_name='Yüz Skalası (0-10)',
        choices=wongBakerFacesPainScaleChoices,
        default=0
    )

    # endregion

    # region behavioral

    # region behavioralFaceExpressionPainScale

    behavioralFaceExpressionPainScaleChoices = [
        (0, '0. Ağrı İfadesi Yok / Gülümsüyor'),
        (1, '1. Nadir Yüz Buruşturma, Çatık Kaş İlgisiz'),
        (2, '2. Sık Sık Çenesini ve Dişlerini Sıkıyor'),
    ]

    behavioralFaceExpressionPainScale = models.PositiveSmallIntegerField(
        verbose_name='Davranışsal Ağrı Skalası - Yüz İfadesi (0-2)',
        choices=behavioralFaceExpressionPainScaleChoices,
        default=0
    )

    # endregion

    # region behavioralLegMovementsPainScale

    behavioralLegMovementsPainScaleChoices = [
        (0, '0. Normal / Rahat Pozisyonda'),
        (1, '1. Huzursuz'),
        (2, '2. Tekmeleme / Bacakları Çekme'),
    ]

    behavioralLegMovementsPainScale = models.PositiveSmallIntegerField(
        verbose_name='Davranışsal Ağrı Skalası - Bacak Hareketleri (0-2)',
        choices=behavioralLegMovementsPainScaleChoices,
        default=0
    )

    # endregion

    # region behavioralActivityPainScale

    behavioralActivityPainScaleChoices = [
        (0, '0. Sakin Yatış / Rahat Pozisyon'),
        (1, '1. Gergin / Kıvranıyor'),
        (2, '2. Hassas / Gergin'),
    ]

    behavioralActivityPainScale = models.PositiveSmallIntegerField(
        verbose_name='Davranışsal Ağrı Skalası - Aktivite (0-2)',
        choices=behavioralActivityPainScaleChoices,
        default=0
    )

    # endregion

    # region behavioralCryPainScale

    behavioralCryPainScaleChoices = [
        (0, '0. Ağlama Yok'),
        (1, '1. Arasıra İnleme / Ağlama'),
        (2, '2. Sürekli Ağlama / Bağırma'),
    ]

    behavioralCryPainScale = models.PositiveSmallIntegerField(
        verbose_name='Davranışsal Ağrı Skalası - Ağlama (0-2)',
        choices=behavioralCryPainScaleChoices,
        default=0
    )

    # endregion

    # region behavioralComfortedPainScale

    behavioralComfortedPainScaleChoices = [
        (0, '0. Memnun / Rahat'),
        (1, '1. Arasıra Çevreden Rahatsız'),
        (2, '2. Avutulması Zor'),
    ]

    behavioralComfortedPainScale = models.PositiveSmallIntegerField(
        verbose_name='Davranışsal Ağrı Skalası - Avutulma (0-2)',
        choices=behavioralComfortedPainScaleChoices,
        default=0
    )

    # endregion

    # endregion

    # endregion

    def __str__(self) -> str:
        return 'Dosya No: ' + str(self.service.dosyano) +' Oda: ' + str(self.service.oda)+' Yatak:' + str(self.service.yatak)
        

    class Meta:
        verbose_name = 'Ağrı Formu'
        verbose_name_plural = 'Ağrı Formları'


class PainScale(models.Model):
    pain = models.ForeignKey(
        Pain,
        on_delete=models.CASCADE,
        verbose_name='Ağrı Formu',
        related_name='painScales',
    )

    description = models.TextField(
        verbose_name='Ağrı Skalası (Numerik Davransal Yüz)'
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat'
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'

    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ağrı Skalası (Numerik Davransal Yüz)'
        verbose_name_plural = 'Ağrı Skala Kayıtları'


class PainPlace(models.Model):
    pain = models.ForeignKey(
        Pain,
        on_delete=models.CASCADE,
        verbose_name='Ağrı Formu'
    )

    description = models.TextField(
        verbose_name='Ağrı''nın Yeri (Hasta''nın Kendi İfadesi / Hemşire''nin Gözlemi)'
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat'
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'

    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ağrı''nın Yeri (Hasta''nın Kendi İfadesi / Hemşire''nin Gözlemi)'
        verbose_name_plural = 'Ağrı Yeri Kayıtları'


class PainSeverity(models.Model):
    pain = models.ForeignKey(
        Pain,
        on_delete=models.CASCADE,
        verbose_name='Ağrı Formu'
    )

    description = models.TextField(
        verbose_name='Ağrı''nın Şiddeti (Skalalardan Uygun Olan Kullanılır)'
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat'
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'

    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ağrı''nın Şiddeti (Skalalardan Uygun Olan Kullanılır)'
        verbose_name_plural = 'Ağrı Şiddeti Kayıtları'


class PainFrequency(models.Model):
    pain = models.ForeignKey(
        Pain,
        on_delete=models.CASCADE,
        verbose_name='Ağrı Formu'
    )

    description = models.TextField(
        verbose_name='Ağrı''nın Sıklığı (Hasta''nın Kendi İfadesi İle)'
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat'
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'

    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ağrı''nın Sıklığı (Hasta''nın Kendi İfadesi İle)'
        verbose_name_plural = 'Ağrı Sıklığı Kayıtları'


class PainNature(models.Model):
    pain = models.ForeignKey(
        Pain,
        on_delete=models.CASCADE,
        verbose_name='Ağrı Formu'
    )

    description = models.TextField(
        verbose_name='Ağrı''nın Niteliği (Hasta''nın Kendi İfadesi İle)'
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat'
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'

    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ağrı''nın Niteliği (Hasta''nın Kendi İfadesi İle)'
        verbose_name_plural = 'Ağrı Niteliği Kayıtları'


class PainFactorAffecting(models.Model):
    pain = models.ForeignKey(
        Pain,
        on_delete=models.CASCADE,
        verbose_name='Ağrı Formu'
    )

    description = models.TextField(
        verbose_name='Ağrı''yı Etkileyen Faktörler (Hasta''nın Kendi İfadesi / Hemşire''nin Gözlemi)'
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat'
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'

    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ağrı''yı Etkileyen Faktörler (Hasta''nın Kendi İfadesi / Hemşire''nin Gözlemi)'
        verbose_name_plural = 'Ağrı Faktör Kayıtları'


class PainTargetedLevel(models.Model):
    pain = models.ForeignKey(
        Pain,
        on_delete=models.CASCADE,
        verbose_name='Ağrı Formu'
    )

    description = models.TextField(
        verbose_name='Hedeflenen Ağrı Düzeyi (Hasta İle İşbirliği Halinde Hemşire Tarafından)'
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat'
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'

    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Hedeflenen Ağrı Düzeyi (Hasta İle İşbirliği Halinde Hemşire Tarafından)'
        verbose_name_plural = 'Hedeflenen Ağrı Düzeyi Kayıtları'


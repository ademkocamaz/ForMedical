from django.db import models
from genotip._model.service import Service
from genotip._model.bed import Bed
from django.conf import settings


class Observation(models.Model):
    bed = models.ForeignKey(
        Bed,
        on_delete=models.DO_NOTHING,
        verbose_name='Yatak ve Oda Bilgileri',
        db_constraint=False,
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.DO_NOTHING,
        verbose_name='Servis Bilgileri',
        db_constraint=False,
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi',
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi',
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name='Kullanıcı',
        db_constraint=False,
    )

    date = models.DateTimeField(
        verbose_name='Tarih/Saat',
    )

    doctor = models.CharField(
        verbose_name="Doktor Adı / Soyadı",
        max_length=100,
        blank=True,
        null=True,
    )

    section = models.CharField(
        verbose_name="Bölüm",
        max_length=100,
        blank=True,
        null=True,
    )

    kilogram = models.CharField(
        verbose_name="Kilo (kg)",
        max_length=100,
        blank=True,
        null=True,
    )

    height = models.CharField(
        verbose_name="Boy (cm)",
        max_length=100,
        blank=True,
        null=True,
    )

    preliminary_diagnosis = models.TextField(
        verbose_name="Ön Tanı / Tanı",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Hemşire Gözlem Formu'
        verbose_name_plural = 'Hemşire Gözlem Formları'


class ObservationDetail(models.Model):
    observation = models.ForeignKey(
        to=Observation,
        on_delete=models.CASCADE,
        verbose_name="Hemşire Gözlem Formu",
    )

    edited = models.DateTimeField(
        auto_now=True,
        verbose_name='Düzenleme Tarihi'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Oluşturulma Tarihi'
    )


class ObservationPageOneDetails(ObservationDetail):
    date = models.DateTimeField(
        verbose_name='Tarih/Saat',
    )

    body_temperature = models.CharField(
        verbose_name="Vücut Isısı",
        max_length=100,
        blank=True,
        null=True,
    )

    pulse = models.CharField(
        verbose_name="Nabız",
        max_length=100,
        blank=True,
        null=True,
    )

    blood_pressure = models.CharField(
        verbose_name="Kan Basıncı",
        max_length=100,
        blank=True,
        null=True,
    )

    number_of_breaths = models.CharField(
        verbose_name="Solunum Sayısı",
        max_length=100,
        blank=True,
        null=True,
    )

    oxygen_saturation = models.CharField(
        verbose_name="Oksijen Satürasyonu",
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Hemşire Gözlem Formu Birinci Sayfa"
        verbose_name_plural = "Hemşire Gözlem Formu Birinci Sayfa Kayıtları"


class ObservationPageTwoDetails(ObservationDetail):
    oral_care = models.DateTimeField(
        verbose_name='Hijyen - Ağız Bakımı - Tarih/Saat',
        blank=True,
        null=True,
    )

    hand_facial_care = models.DateTimeField(
        verbose_name='Hijyen - El/Yüz Bakımı - Tarih/Saat',
        blank=True,
        null=True,
    )

    body_bath = models.DateTimeField(
        verbose_name='Hijyen - Vücut Banyosu - Tarih/Saat',
        blank=True,
        null=True,
    )

    perineal_care = models.DateTimeField(
        verbose_name='Hijyen - Perine Bakımı - Tarih/Saat',
        blank=True,
        null=True,
    )

    toenail_care = models.DateTimeField(
        verbose_name='Hijyen - Ayak/Tırnak Bakımı - Tarih/Saat',
        blank=True,
        null=True,
    )

    dressing_change = models.DateTimeField(
        verbose_name='Hijyen - Pansuman Değişimi - Tarih/Saat',
        blank=True,
        null=True,
    )


class ObservationTracking(ObservationDetail):
    planning = models.DateTimeField(
        verbose_name='Planlama - Tarih/Saat',
    )

    implementation = models.DateTimeField(
        verbose_name='Uygulama - Tarih/Saat',
    )


class ObservationTracking_PTaPTT(ObservationTracking):
    class Meta:
        verbose_name = "PT/aPTT Takibi"
        verbose_name_plural = "PT/aPTT Kayıtları"


class ObservationTracking_Hemogram(ObservationTracking):
    class Meta:
        verbose_name = "Hemogram Takibi"
        verbose_name_plural = "Hemogram Kayıtları"


class ObservationTracking_BreathingExercise(ObservationTracking):
    class Meta:
        verbose_name = "Solunum Egzersizi"
        verbose_name_plural = "Solunum Egzersizi Kayıtları"


class ObservationTracking_CVP(ObservationTracking):
    class Meta:
        verbose_name = "CVP Takibi"
        verbose_name_plural = "CVP Kayıtları"


class ObservationTracking_SteamTreatment(ObservationTracking):
    class Meta:
        verbose_name = "Buhar Tedavisi"
        verbose_name_plural = "Buhar Tedavisi Kayıtları"


class ObservationTracking_Aspiration(ObservationTracking):
    class Meta:
        verbose_name = "Aspirasyon"
        verbose_name_plural = "Aspirasyon Kayıtları"


class ObservationTracking_EKG(ObservationTracking):
    class Meta:
        verbose_name = "EKG Çekimi"
        verbose_name_plural = "EKG Kayıtları"


class ObservationTracking_SandBagApplication(ObservationTracking):
    class Meta:
        verbose_name = "Kum Torbası Uygulaması"
        verbose_name_plural = "Kum Torbası Uygulama Kayıtları"


class ObservationTracking_IceBagApplication(ObservationTracking):
    class Meta:
        verbose_name = "Buz Torbası Uygulaması"
        verbose_name_plural = "Buz Torbası Uygulama Kayıtları"


class ObservationTracking_ColdHotApplication(ObservationTracking):
    class Meta:
        verbose_name = "Soğuk-Sıcak Uygulama"
        verbose_name_plural = "Soğuk-Sıcak Uygulama Kayıtları"


class ObservationTracking_GodePlus(ObservationTracking):
    class Meta:
        verbose_name = "Gode+"
        verbose_name_plural = "Gode+ Kayıtları"


class ObservationTracking_GodePlusPlus(ObservationTracking):
    class Meta:
        verbose_name = "Gode++"
        verbose_name_plural = "Gode++ Kayıtları"


class ObservationTracking_GodePlusPlusPlus(ObservationTracking):
    class Meta:
        verbose_name = "Gode+++"
        verbose_name_plural = "Gode+++ Kayıtları"


class ObservationTracking_RadiologicalExamination(ObservationTracking):
    examination_name = models.CharField(
        verbose_name="Tetkik Adı",
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Radyolojik İnceleme"
        verbose_name_plural = "Radyolojik İnceleme Kayıtları"


class ObservationInsertionOpening(ObservationDetail):
    cvp_catheter = models.DateTimeField(
        verbose_name='Takılma / Açılma - CVP Kateteri - Tarih/Saat',
        blank=True,
        null=True,
    )

    urinary_catheter = models.DateTimeField(
        verbose_name='Takılma / Açılma - Üriner Kateter - Tarih/Saat',
        blank=True,
        null=True,
    )

    peripheral_catheter = models.DateTimeField(
        verbose_name='Takılma / Açılma - Periferik Kateter - Tarih/Saat',
        blank=True,
        null=True,
    )

    urinary_catheter = models.DateTimeField(
        verbose_name='Takılma / Açılma - NG Sonda - Tarih/Saat',
        blank=True,
        null=True,
    )


class ObservationNote(ObservationDetail):
    note = models.TextField(
        verbose_name="Hemşire İzlem Notu",
    )

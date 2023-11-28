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

    # aşağıdaki 3 alan zaten hasta bilgilerinde geliyor ve tarih created olarak zaten alıyoruz

    # date = models.DateTimeField(
    #     verbose_name='Tarih/Saat',
    # )

    # doctor = models.CharField(
    #     verbose_name="Doktor Adı / Soyadı",
    #     max_length=100,
    #     blank=True,
    #     null=True,
    # )

    # section = models.CharField(
    #     verbose_name="Bölüm",
    #     max_length=100,
    #     blank=True,
    #     null=True,
    # )

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
        verbose_name='Ağız Bakımı - Uygulama Tarih/Saat',
        blank=True,
        null=True,
    )

    hand_facial_care = models.DateTimeField(
        verbose_name='El/Yüz Bakımı - Uygulama Tarih/Saat',
        blank=True,
        null=True,
    )

    body_bath = models.DateTimeField(
        verbose_name='Vücut Banyosu - Uygulama Tarih/Saat',
        blank=True,
        null=True,
    )

    perineal_care = models.DateTimeField(
        verbose_name='Perine Bakımı - Uygulama Tarih/Saat',
        blank=True,
        null=True,
    )

    toenail_care = models.DateTimeField(
        verbose_name='Ayak/Tırnak Bakımı - Uygulama Tarih/Saat',
        blank=True,
        null=True,
    )

    dressing_change = models.DateTimeField(
        verbose_name='Pansuman Değişimi - Uygulama Tarih/Saat',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Hijyen Bakımı"
        verbose_name_plural = "Hijyen Bakım Kayıtları"


class ObservationTracking(ObservationDetail):
    planning = models.DateTimeField(
        verbose_name='Planlama - Tarih/Saat',
        blank=True,
        null=True,
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
        verbose_name='CVP Kateteri - Tarih/Saat',
        blank=True,
        null=True,
    )

    urinary_catheter = models.DateTimeField(
        verbose_name='Üriner Kateter - Tarih/Saat',
        blank=True,
        null=True,
    )

    peripheral_catheter = models.DateTimeField(
        verbose_name='Periferik Kateter - Tarih/Saat',
        blank=True,
        null=True,
    )

    urinary_catheter = models.DateTimeField(
        verbose_name='NG Sonda - Tarih/Saat',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Takılma / Açılma"
        verbose_name_plural = "Takılma / Açılma Kayıtları"


class ObservationNote(ObservationDetail):
    note = models.TextField(
        verbose_name="Hemşire İzlem Notu",
    )

    class Meta:
        verbose_name="Hemşire İzlem Notu"
        verbose_name_plural="Hemşire İzlem Notu Kayıtları"
        

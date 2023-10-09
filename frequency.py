# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ViewGenotipGelisler(models.Model):
    dosyano = models.CharField(db_column='DOSYANO', max_length=15)  # Field name made lowercase.
    gelisno = models.SmallIntegerField(db_column='GELISNO')  # Field name made lowercase.
    giristarih = models.DateTimeField(db_column='GIRISTARIH', blank=True, null=True)  # Field name made lowercase.
    cikistarih = models.DateTimeField(db_column='CIKISTARIH', blank=True, null=True)  # Field name made lowercase.
    yatgunsay = models.SmallIntegerField(db_column='YATGUNSAY', blank=True, null=True)  # Field name made lowercase.
    tedavi = models.CharField(db_column='TEDAVI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    kurum = models.CharField(db_column='KURUM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referans = models.CharField(db_column='REFERANS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    referanskod = models.CharField(db_column='REFERANSKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    poliklinik = models.CharField(db_column='POLIKLINIK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doktorkod = models.CharField(db_column='DOKTORKOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    doktor = models.CharField(db_column='DOKTOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    katkiyuzde = models.FloatField(db_column='KATKIYUZDE', blank=True, null=True)  # Field name made lowercase.
    hesap = models.CharField(db_column='HESAP', max_length=6, blank=True, null=True)  # Field name made lowercase.
    kdvdurum = models.CharField(db_column='KDVDURUM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    faturatarih = models.DateTimeField(db_column='FATURATARIH', blank=True, null=True)  # Field name made lowercase.
    faturano = models.CharField(db_column='FATURANO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    faturatarih2 = models.DateTimeField(db_column='FATURATARIH2', blank=True, null=True)  # Field name made lowercase.
    faturano2 = models.CharField(db_column='FATURANO2', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kalan_bakiye = models.CharField(db_column='KALAN_BAKIYE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kullanici = models.CharField(db_column='KULLANICI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    onay = models.CharField(db_column='ONAY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isk_isteyen = models.CharField(db_column='ISK_ISTEYEN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    protokolno = models.CharField(db_column='PROTOKOLNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sevkno = models.CharField(db_column='SEVKNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sevkbastarihi = models.DateTimeField(db_column='SEVKBASTARIHI', blank=True, null=True)  # Field name made lowercase.
    sevkbitistarihi = models.DateTimeField(db_column='SEVKBITISTARIHI', blank=True, null=True)  # Field name made lowercase.
    provizyon = models.CharField(db_column='PROVIZYON', max_length=25, blank=True, null=True)  # Field name made lowercase.
    icdkodu = models.CharField(db_column='ICDKODU', max_length=100, blank=True, null=True)  # Field name made lowercase.
    icdadi = models.CharField(db_column='ICDADI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    icmaldokumu = models.CharField(db_column='ICMALDOKUMU', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tiplitanikodu = models.CharField(db_column='TIPLITANIKODU', max_length=100, blank=True, null=True)  # Field name made lowercase.
    takipno = models.CharField(db_column='TAKIPNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sevktakipno = models.CharField(db_column='SEVKTAKIPNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gsssorgudurum = models.CharField(db_column='GSSSORGUDURUM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    taburcukodu = models.CharField(db_column='TABURCUKODU', max_length=2, blank=True, null=True)  # Field name made lowercase.
    istisnaidurum = models.CharField(db_column='ISTISNAIDURUM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sonuc = models.CharField(db_column='SONUC', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    eklenmetarih = models.CharField(db_column='EKLENMETARIH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    icmalsira = models.IntegerField(db_column='ICMALSIRA', blank=True, null=True)  # Field name made lowercase.
    onicmalno = models.CharField(db_column='ONICMALNO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    provizyonturu = models.CharField(db_column='PROVIZYONTURU', max_length=20, blank=True, null=True)  # Field name made lowercase.
    takipturu = models.CharField(db_column='TAKIPTURU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    raportakipno = models.CharField(db_column='RAPORTAKIPNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sevkedenklinik = models.CharField(db_column='SEVKEDENKLINIK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vakaturu = models.CharField(db_column='VAKATURU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sevktarihi = models.DateTimeField(db_column='SEVKTARIHI', blank=True, null=True)  # Field name made lowercase.
    yatisinaciliyeti = models.CharField(db_column='YATISINACILIYETI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sevkedendoktor = models.CharField(db_column='SEVKEDENDOKTOR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ekleyen = models.CharField(db_column='EKLEYEN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kabulsekli = models.CharField(db_column='KABULSEKLI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    polkod = models.CharField(db_column='POLKOD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basvuruno = models.CharField(db_column='BASVURUNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sn_satir_degisti = models.BooleanField(db_column='SN_SATIR_DEGISTI', blank=True, null=True)  # Field name made lowercase.
    sn_butunluk_degisti = models.BooleanField(db_column='SN_BUTUNLUK_DEGISTI', blank=True, null=True)  # Field name made lowercase.
    sn_satir_degistirme_tarihi = models.DateTimeField(db_column='SN_SATIR_DEGISTIRME_TARIHI', blank=True, null=True)  # Field name made lowercase.
    sevkkabuledenbrans = models.CharField(db_column='SEVKKABULEDENBRANS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sevkturu = models.CharField(db_column='SEVKTURU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    arsiv = models.BooleanField(db_column='ARSIV', blank=True, null=True)  # Field name made lowercase.
    medulateslimno = models.CharField(db_column='MEDULATESLIMNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    medulafaturatarihi = models.DateTimeField(db_column='MEDULAFATURATARIHI', blank=True, null=True)  # Field name made lowercase.
    tedavitipi = models.CharField(db_column='TEDAVITIPI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    medulasec = models.BooleanField(db_column='MEDULASEC', blank=True, null=True)  # Field name made lowercase.
    icmalno = models.CharField(db_column='ICMALNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kontroltakibi = models.BooleanField(db_column='KONTROLTAKIBI', blank=True, null=True)  # Field name made lowercase.
    disrad = models.CharField(db_column='DISRAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    medulafaturakullanici = models.CharField(db_column='MEDULAFATURAKULLANICI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sube = models.CharField(db_column='SUBE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ucretlendirmetarih = models.DateTimeField(db_column='UCRETLENDIRMETARIH', blank=True, null=True)  # Field name made lowercase.
    ucretlendiren = models.CharField(db_column='UCRETLENDIREN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taburcutarihi = models.DateTimeField(db_column='TABURCUTARIHI', blank=True, null=True)  # Field name made lowercase.
    webprint = models.SmallIntegerField(db_column='WEBPRINT', blank=True, null=True)  # Field name made lowercase.
    sat = models.CharField(db_column='SAT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    medulatakiptarihi = models.DateTimeField(db_column='MEDULATAKIPTARIHI', blank=True, null=True)  # Field name made lowercase.
    vaka112 = models.BooleanField(db_column='VAKA112', blank=True, null=True)  # Field name made lowercase.
    vaka112pno = models.IntegerField(db_column='VAKA112PNO', blank=True, null=True)  # Field name made lowercase.
    vaka112sonuc = models.CharField(db_column='VAKA112SONUC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    medulasube_id = models.IntegerField(db_column='MEDULASUBE_ID', blank=True, null=True)  # Field name made lowercase.
    sube_id = models.IntegerField(db_column='SUBE_ID', blank=True, null=True)  # Field name made lowercase.
    gondoktorkod = models.CharField(db_column='GONDOKTORKOD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kontrolgelisi = models.SmallIntegerField(db_column='KONTROLGELISI', blank=True, null=True)  # Field name made lowercase.
    gondoktor = models.CharField(db_column='GONDOKTOR', max_length=150, blank=True, null=True)  # Field name made lowercase.
    medulaornekleme = models.BooleanField(db_column='MEDULAORNEKLEME', blank=True, null=True)  # Field name made lowercase.
    medulaornekevrakno = models.CharField(db_column='MEDULAORNEKEVRAKNO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    aciktahsilatonay = models.BooleanField(db_column='ACIKTAHSILATONAY', blank=True, null=True)  # Field name made lowercase.
    medulaicmalno = models.CharField(db_column='MEDULAICMALNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rahatsizlik = models.SmallIntegerField(db_column='RAHATSIZLIK', blank=True, null=True)  # Field name made lowercase.
    medulafaturatutaroku = models.BooleanField(db_column='MEDULAFATURATUTAROKU', blank=True, null=True)  # Field name made lowercase.
    medulafaturaiptalsayac = models.SmallIntegerField(db_column='MEDULAFATURAIPTALSAYAC', blank=True, null=True)  # Field name made lowercase.
    medulatakipkullanici = models.CharField(db_column='MEDULATAKIPKULLANICI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    isk_isteyenbilgi = models.CharField(db_column='ISK_ISTEYENBILGI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    akisadimid = models.IntegerField(db_column='AKISADIMID', blank=True, null=True)  # Field name made lowercase.
    akissirano = models.IntegerField(db_column='AKISSIRANO', blank=True, null=True)  # Field name made lowercase.
    labonaysmsgonderim = models.BooleanField(db_column='LABONAYSMSGONDERIM', blank=True, null=True)  # Field name made lowercase.
    taahhutname = models.BooleanField(db_column='TAAHHUTNAME', blank=True, null=True)  # Field name made lowercase.
    plakano = models.CharField(db_column='PLAKANO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    snmuaturu = models.CharField(db_column='SNMUATURU', max_length=2, blank=True, null=True)  # Field name made lowercase.
    snprotokolno = models.IntegerField(db_column='SNPROTOKOLNO', blank=True, null=True)  # Field name made lowercase.
    sevkedentesiskodu = models.CharField(db_column='SEVKEDENTESISKODU', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sevkedilenbranskodu = models.CharField(db_column='SEVKEDILENBRANSKODU', max_length=10, blank=True, null=True)  # Field name made lowercase.
    evrakarsivno = models.CharField(db_column='EVRAKARSIVNO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    yesilalan = models.BooleanField(db_column='YESILALAN', blank=True, null=True)  # Field name made lowercase.
    trafikkazaodemeyuzde = models.IntegerField(db_column='TRAFIKKAZAODEMEYUZDE', blank=True, null=True)  # Field name made lowercase.
    hakedisdurum = models.SmallIntegerField(db_column='HAKEDISDURUM', blank=True, null=True)  # Field name made lowercase.
    hakedistarihi = models.DateTimeField(db_column='HAKEDISTARIHI', blank=True, null=True)  # Field name made lowercase.
    hakedisonaylayan = models.CharField(db_column='HAKEDISONAYLAYAN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hakedisiptaleden = models.CharField(db_column='HAKEDISIPTALEDEN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    triajbeyani = models.CharField(db_column='TRIAJBEYANI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    adlivakagelissekli = models.SmallIntegerField(db_column='ADLIVAKAGELISSEKLI', blank=True, null=True)  # Field name made lowercase.
    ambulansilegelisdurumu = models.SmallIntegerField(db_column='AMBULANSILEGELISDURUMU', blank=True, null=True)  # Field name made lowercase.
    sevkedengelis = models.SmallIntegerField(db_column='SEVKEDENGELIS', blank=True, null=True)  # Field name made lowercase.
    yesilkartsevkedentedavitipi = models.CharField(db_column='YESILKARTSEVKEDENTEDAVITIPI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    yesilkartsevkedentakiptipi = models.CharField(db_column='YESILKARTSEVKEDENTAKIPTIPI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    istisnaihal = models.CharField(db_column='ISTISNAIHAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ykresigno = models.CharField(db_column='YKRESIGNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ibraname_doldurun = models.CharField(db_column='IBRANAME_DOLDURUN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yatistipi = models.SmallIntegerField(db_column='YATISTIPI', blank=True, null=True)  # Field name made lowercase.
    ftrseanssayisi = models.SmallIntegerField(db_column='FTRSEANSSAYISI', blank=True, null=True)  # Field name made lowercase.
    biyometrikdogrulama = models.BooleanField(db_column='BIYOMETRIKDOGRULAMA', blank=True, null=True)  # Field name made lowercase.
    medulayardimhakkiid = models.IntegerField(db_column='MEDULAYARDIMHAKKIID', blank=True, null=True)  # Field name made lowercase.
    provtarihi = models.DateTimeField(db_column='PROVTARIHI', blank=True, null=True)  # Field name made lowercase.
    evrakteslimeden = models.CharField(db_column='EVRAKTESLIMEDEN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    evrakteslimalan = models.CharField(db_column='EVRAKTESLIMALAN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    evrakstatu = models.CharField(db_column='EVRAKSTATU', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sonuckilitli = models.BooleanField(db_column='SONUCKILITLI', blank=True, null=True)  # Field name made lowercase.
    katkiistisna = models.SmallIntegerField(db_column='KATKIISTISNA', blank=True, null=True)  # Field name made lowercase.
    muhaktar = models.SmallIntegerField(db_column='MUHAKTAR', blank=True, null=True)  # Field name made lowercase.
    dovizcinsi = models.CharField(db_column='DOVIZCINSI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dovizkuru = models.DecimalField(db_column='DOVIZKURU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    medulahatanedeni = models.SmallIntegerField(db_column='MEDULAHATANEDENI', blank=True, null=True)  # Field name made lowercase.
    medulahatakullanici = models.CharField(db_column='MEDULAHATAKULLANICI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tercihlirandevu = models.BooleanField(db_column='TERCIHLIRANDEVU', blank=True, null=True)  # Field name made lowercase.
    kurumprotokolno = models.CharField(db_column='KURUMPROTOKOLNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eklemetarihi = models.DateTimeField(db_column='EKLEMETARIHI', blank=True, null=True)  # Field name made lowercase.
    degistiren = models.CharField(db_column='DEGISTIREN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    degistirmetarihi = models.DateTimeField(db_column='DEGISTIRMETARIHI', blank=True, null=True)  # Field name made lowercase.
    karaliste = models.BooleanField(db_column='KARALISTE', blank=True, null=True)  # Field name made lowercase.
    siramatikdurum = models.CharField(db_column='SIRAMATIKDURUM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gelisrumuz = models.CharField(db_column='GELISRUMUZ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    radsonuctarih = models.DateTimeField(db_column='RADSONUCTARIH', blank=True, null=True)  # Field name made lowercase.
    labsonuctarih = models.DateTimeField(db_column='LABSONUCTARIH', blank=True, null=True)  # Field name made lowercase.
    devredilenkurum = models.CharField(db_column='DEVREDILENKURUM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vakatarihi = models.DateTimeField(db_column='VAKATARIHI', blank=True, null=True)  # Field name made lowercase.
    medulaorneklemegrupturu = models.CharField(db_column='MEDULAORNEKLEMEGRUPTURU', max_length=1, blank=True, null=True)  # Field name made lowercase.
    medulaorneklemegrupkodu = models.SmallIntegerField(db_column='MEDULAORNEKLEMEGRUPKODU', blank=True, null=True)  # Field name made lowercase.
    randevukaynak = models.SmallIntegerField(db_column='RANDEVUKAYNAK', blank=True, null=True)  # Field name made lowercase.
    snsgkiletimtipi = models.SmallIntegerField(db_column='SNSGKILETIMTIPI', blank=True, null=True)  # Field name made lowercase.
    kimlikid = models.IntegerField(db_column='KIMLIKID', blank=True, null=True)  # Field name made lowercase.
    kurumid = models.IntegerField(db_column='KURUMID', blank=True, null=True)  # Field name made lowercase.
    polid = models.IntegerField(db_column='POLID', blank=True, null=True)  # Field name made lowercase.
    doktorid = models.IntegerField(db_column='DOKTORID', blank=True, null=True)  # Field name made lowercase.
    gondoktorid = models.IntegerField(db_column='GONDOKTORID', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    bimno = models.IntegerField(db_column='BIMNO')  # Field name made lowercase.
    donor_alici_kimlik_numarasi = models.CharField(db_column='DONOR_ALICI_KIMLIK_NUMARASI', max_length=11, blank=True, null=True)  # Field name made lowercase.
    faturanakittutar = models.CharField(db_column='FATURANAKITTUTAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kvkkonaykodu = models.CharField(db_column='KVKKONAYKODU', max_length=10, blank=True, null=True)  # Field name made lowercase.
    temasdurumsorgulama = models.BooleanField(db_column='TEMASDURUMSORGULAMA', blank=True, null=True)  # Field name made lowercase.
    kvkkonaytarihi = models.DateTimeField(db_column='KVKKONAYTARIHI', blank=True, null=True)  # Field name made lowercase.
    covid19skrskulke = models.IntegerField(db_column='COVID19SKRSKULKE', blank=True, null=True)  # Field name made lowercase.
    covid19tarih = models.DateTimeField(db_column='COVID19TARIH', blank=True, null=True)  # Field name made lowercase.
    sirgirsaat = models.CharField(db_column='SIRGIRSAAT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sirciksaat = models.CharField(db_column='SIRCIKSAAT', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VIEW_GENOTIP_GELISLER'

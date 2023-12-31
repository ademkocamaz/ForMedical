SELECT
    GEN2000.dbo.YATAKDURUM.ID,
    GEN2000.dbo.SERVISLER.AD AS SERVIS_ADI,
    GEN2000.dbo.YATAKDURUM.ODA,
    GEN2000.dbo.YATAKDURUM.YATAK,
    GEN2000.dbo.YATAKDURUM.SERVISID AS SERVISTANIMID,
    GEN2000.dbo.YATAKDURUM.DURUM,
    GEN2000.dbo.YATAKDURUM.DOSYANO,
    GEN2000.dbo.YATAKDURUM.GELISNO,
    GEN2000.dbo.SERVIS.ID AS SERVISID
FROM
    GEN2000.dbo.SERVIS
    INNER JOIN GEN2000.dbo.SERVISLER
    INNER JOIN GEN2000.dbo.YATAKDURUM ON GEN2000.dbo.SERVISLER.ID = GEN2000.dbo.YATAKDURUM.SERVISID ON GEN2000.dbo.SERVIS.DOSYANO = GEN2000.dbo.YATAKDURUM.DOSYANO
    AND GEN2000.dbo.SERVIS.GELISNO = GEN2000.dbo.YATAKDURUM.GELISNO
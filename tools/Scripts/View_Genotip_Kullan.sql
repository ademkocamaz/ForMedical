SELECT
    ID,
    KULLANICIADI,
    SIFRE,
    KULLANICI,
    SUPER,
    -- CASE
    --     WHEN PASIF = 1 THEN 'True'
    --     WHEN PASIF = 0 THEN 'False'
    -- END AS Expr1,
    GRUP
FROM
    GEN2000.dbo.KULLAN
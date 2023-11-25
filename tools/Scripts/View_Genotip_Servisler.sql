SELECT
    ID,
    AD,
    AKTIF
FROM
    GEN2000.dbo.SERVISLER
WHERE
    (
        ID IN (
            SELECT
                SERVISLER_JOIN.ID
            FROM
                GEN2000.dbo.SERVISLER AS SERVISLER_JOIN
                INNER JOIN GEN2000.dbo.YATAKDURUM ON SERVISLER_JOIN.ID = GEN2000.dbo.YATAKDURUM.SERVISID
        )
    )
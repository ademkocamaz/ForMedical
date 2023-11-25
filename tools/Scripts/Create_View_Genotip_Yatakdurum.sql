USE [FORMEDICAL]
GO

/****** Object:  View [dbo].[VIEW_GENOTIP_YATAKDURUM]    Script Date: 25.11.2023 21:47:48 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[VIEW_GENOTIP_YATAKDURUM]
AS
SELECT        GEN2000.dbo.YATAKDURUM.ID, GEN2000.dbo.SERVISLER.AD AS SERVIS_ADI, GEN2000.dbo.YATAKDURUM.ODA, GEN2000.dbo.YATAKDURUM.YATAK, GEN2000.dbo.YATAKDURUM.SERVISID AS SERVISTANIMID, 
                         GEN2000.dbo.YATAKDURUM.DURUM, GEN2000.dbo.YATAKDURUM.DOSYANO, GEN2000.dbo.YATAKDURUM.GELISNO, GEN2000.dbo.SERVIS.ID AS SERVISID
FROM            GEN2000.dbo.SERVIS INNER JOIN
                         GEN2000.dbo.SERVISLER INNER JOIN
                         GEN2000.dbo.YATAKDURUM ON GEN2000.dbo.SERVISLER.ID = GEN2000.dbo.YATAKDURUM.SERVISID ON GEN2000.dbo.SERVIS.DOSYANO = GEN2000.dbo.YATAKDURUM.DOSYANO AND 
                         GEN2000.dbo.SERVIS.GELISNO = GEN2000.dbo.YATAKDURUM.GELISNO
GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[41] 4[20] 2[8] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "SERVISLER (GEN2000.dbo)"
            Begin Extent = 
               Top = 6
               Left = 38
               Bottom = 312
               Right = 275
            End
            DisplayFlags = 280
            TopColumn = 7
         End
         Begin Table = "YATAKDURUM (GEN2000.dbo)"
            Begin Extent = 
               Top = 6
               Left = 313
               Bottom = 338
               Right = 502
            End
            DisplayFlags = 280
            TopColumn = 14
         End
         Begin Table = "SERVIS (GEN2000.dbo)"
            Begin Extent = 
               Top = 6
               Left = 540
               Bottom = 293
               Right = 901
            End
            DisplayFlags = 280
            TopColumn = 21
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
      Begin ColumnWidths = 10
         Width = 284
         Width = 1500
         Width = 1965
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 1725
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'VIEW_GENOTIP_YATAKDURUM'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'VIEW_GENOTIP_YATAKDURUM'
GO



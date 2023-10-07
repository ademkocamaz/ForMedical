/*
This Script Creates a SQL Server Database, Login and User
With Appropriate Permissions for a Production Django Project
with migrations. Simply fill out the variables below (@db_name and @db_password)
Username will be set to database name + '_user' by default.
*/
DECLARE @db_name VARCHAR(MAX) = 'FORMEDICAL'
DECLARE @db_password VARCHAR(MAX) = '764864'
DECLARE @db_user VARCHAR(MAX) = @db_name + 'ForMedical'
--
--
USE master
DECLARE @cmd VARCHAR(MAX)
-- Server scope: create SQL Server login and permissions
SET @cmd = 'CREATE LOGIN ' + @db_user + ' WITH PASSWORD = ''' + @db_password + ''''
EXEC(@cmd)
SET @cmd = 'GRANT VIEW SERVER STATE TO ' + @db_user
EXEC(@cmd)
SET @cmd = 'CREATE DATABASE [' + @db_name + ']'
EXEC(@cmd)
-- DB scope: create user for server login and permissions
SET @cmd = 'USE [' + @db_name + '];'
SET @cmd = @cmd + 'CREATE USER ' + @db_user + ' FOR LOGIN ' + @db_user + ';'
SET @cmd = @cmd + 'GRANT SELECT, INSERT, UPDATE, DELETE, ALTER, CREATE TABLE, REFERENCES, EXEC TO ' + @db_user
EXEC(@cmd)
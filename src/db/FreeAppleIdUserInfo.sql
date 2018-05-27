CREATE DATABASE IF NOT EXISTS FreeAppleIdDB;

USE FreeAppleIdDB;

DROP TABLE IF EXISTS FreeAppleIdUserInfo;

CREATE TABLE IF NOT EXISTS FreeAppleIdUserInfo
(
    Id_P int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userEmail varchar(255) NOT NULL UNIQUE,
    applePassword varchar(255) NOT NULL,

    LastName varchar(255),
    FirstName varchar(255),
    BirthDay date,
    Address varchar(255),
    City varchar(255)
);
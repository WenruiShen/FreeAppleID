CREATE DATABASE IF NOT EXISTS FreeAppleIdDB;
USE FreeAppleIdDB;

CREATE TABLE FreeAppleIdUserInfo
(
    Id_P int NOT NULL PRIMARY KEY,
    userEmail varchar(255) NOT NULL UNIQUE,
    applePassword varchar(255) NOT NULL,

    LastName varchar(255),
    FirstName varchar(255),
    BirthDay date,
    Address varchar(255),
    City varchar(255)
);
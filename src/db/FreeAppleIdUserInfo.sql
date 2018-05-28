CREATE DATABASE IF NOT EXISTS FreeAppleIdDB;

USE FreeAppleIdDB;

DROP TABLE IF EXISTS FreeAppleIdUserInfo;

CREATE TABLE IF NOT EXISTS FreeAppleIdUserInfo
(
    Id_P          int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userEmail     varchar(255) NOT NULL UNIQUE,
    applePassword varchar(255) NOT NULL,

    LastName      varchar(255) NOT NULL,
    FirstName     varchar(255) NOT NULL,
    BirthDay      date NOT NULL,

    create_time   timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    update_time   timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
);
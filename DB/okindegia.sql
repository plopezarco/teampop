CREATE DATABASE  IF NOT EXISTS `okindegia` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `okindegia`;
-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: okindegia
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `banatzailea`
--

DROP TABLE IF EXISTS `banatzailea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banatzailea` (
  `id_banatzailea` int NOT NULL,
  `nan` varchar(9) NOT NULL,
  `izena` varchar(45) DEFAULT NULL,
  `abizena` varchar(45) DEFAULT NULL,
  `libre_dago` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_banatzailea`),
  UNIQUE KEY `nan_UNIQUE` (`nan`),
  UNIQUE KEY `id_banatzailea_UNIQUE` (`id_banatzailea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banatzailea`
--

LOCK TABLES `banatzailea` WRITE;
/*!40000 ALTER TABLE `banatzailea` DISABLE KEYS */;
INSERT INTO `banatzailea` VALUES (1,'12345678A','Reparti1','Repar',_binary '\0');
/*!40000 ALTER TABLE `banatzailea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bezeroak`
--

DROP TABLE IF EXISTS `bezeroak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bezeroak` (
  `id_bezeroa` int NOT NULL AUTO_INCREMENT,
  `izena` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `telefonoa` varchar(9) DEFAULT NULL,
  PRIMARY KEY (`id_bezeroa`),
  UNIQUE KEY `id_bezeroa_UNIQUE` (`id_bezeroa`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bezeroak`
--

LOCK TABLES `bezeroak` WRITE;
/*!40000 ALTER TABLE `bezeroak` DISABLE KEYS */;
INSERT INTO `bezeroak` VALUES (1,'Pablo','pablo@mail.com','123456789');
/*!40000 ALTER TABLE `bezeroak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produktuak`
--

DROP TABLE IF EXISTS `produktuak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produktuak` (
  `id_produktua` int NOT NULL AUTO_INCREMENT,
  `izena` varchar(45) DEFAULT NULL,
  `prezioa` double DEFAULT NULL,
  PRIMARY KEY (`id_produktua`),
  UNIQUE KEY `id_produktua_UNIQUE` (`id_produktua`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produktuak`
--

LOCK TABLES `produktuak` WRITE;
/*!40000 ALTER TABLE `produktuak` DISABLE KEYS */;
INSERT INTO `produktuak` VALUES (1,'Pastela',10);
/*!40000 ALTER TABLE `produktuak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `id_ticket` int NOT NULL AUTO_INCREMENT,
  `id_bezeroa` int NOT NULL,
  `data` datetime DEFAULT NULL,
  `totala` double DEFAULT NULL,
  `id_banatzailea` int NOT NULL,
  PRIMARY KEY (`id_ticket`,`id_bezeroa`),
  KEY `fk_eskaerak_bezeroak_idx` (`id_bezeroa`),
  KEY `fk_ticket_banatzailea1_idx` (`id_banatzailea`),
  CONSTRAINT `fk_eskaerak_bezeroak` FOREIGN KEY (`id_bezeroa`) REFERENCES `bezeroak` (`id_bezeroa`),
  CONSTRAINT `fk_ticket_banatzailea1` FOREIGN KEY (`id_banatzailea`) REFERENCES `banatzailea` (`id_banatzailea`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,1,NULL,10,1);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_lerroak`
--

DROP TABLE IF EXISTS `ticket_lerroak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket_lerroak` (
  `id_ticket` int NOT NULL,
  `id_produktua` int NOT NULL,
  `kantitatea` varchar(45) DEFAULT NULL,
  `subtotala` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_ticket`,`id_produktua`),
  KEY `fk_ticket_lerroak_produktuak1_idx` (`id_produktua`),
  KEY `fk_ticket_lerroak_ticket1_idx` (`id_ticket`),
  CONSTRAINT `fk_ticket_lerroak_produktuak1` FOREIGN KEY (`id_produktua`) REFERENCES `produktuak` (`id_produktua`),
  CONSTRAINT `fk_ticket_lerroak_ticket1` FOREIGN KEY (`id_ticket`) REFERENCES `ticket` (`id_ticket`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_lerroak`
--

LOCK TABLES `ticket_lerroak` WRITE;
/*!40000 ALTER TABLE `ticket_lerroak` DISABLE KEYS */;
INSERT INTO `ticket_lerroak` VALUES (1,1,'1','10');
/*!40000 ALTER TABLE `ticket_lerroak` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-27  8:26:41

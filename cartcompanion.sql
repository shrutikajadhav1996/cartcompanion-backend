-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cartcompanion
-- ------------------------------------------------------
-- Server version	8.0.38

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
-- Table structure for table `dress`
--

DROP TABLE IF EXISTS `dress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dress` (
  `DressID` int NOT NULL,
  `DressType` varchar(70) NOT NULL,
  `Dress` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Price` int NOT NULL,
  `Stock` varchar(45) NOT NULL,
  PRIMARY KEY (`DressID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dress`
--

LOCK TABLES `dress` WRITE;
/*!40000 ALTER TABLE `dress` DISABLE KEYS */;
INSERT INTO `dress` VALUES (1,'Yellow Short Dress','small','women',30,'Instock'),(2,'Yellow Short Dress','medium','women',30,'Instock'),(3,'Yellow Short Dress','large','women',30,'Instock'),(4,'Yellow Short Dress','extra large','women',30,'Instock'),(5,'Blue Short Dress','small','women',25,'out of stock'),(6,'Blue Short Dress','medium','women',25,'Instock'),(7,'Blue Short Dress','large','women',25,'Instock'),(8,'Blue Short Dress','extra large','women',25,'Instock'),(9,'Golden Party Gown','small','women',50,'Instock'),(10,'Golden Party Gown','medium','women',50,'Instock'),(11,'Golden Party Gown','large','women',50,'Instock'),(12,'Golden Party Gown','extra large','women',50,'Instock'),(13,'Floral dress','small','women',20,'Instock'),(14,'Floral dress','medium','women',20,'Instock'),(15,'Floral dress','large','women',20,'Instock'),(16,'Floral dress','extra large','women',20,'out of stock'),(17,'Black short dress','small','women',15,'Instock'),(18,'Black short dress','medium','women',15,'Instock'),(19,'Black short dress','large','women',15,'Instock'),(20,'Black short dress','extra large','women',15,'Instock'),(21,'Pink Formal shirt with pant','small','men',50,'Instock'),(22,'Pink Formal shirt with pant','medium','men',50,'Instock'),(23,'Pink Formal shirt with pant','large','men',50,'Instock'),(24,'Pink Formal shirt with pant','extra large','men',50,'Instock'),(25,'Grey Suit','small','men',80,'Instock'),(26,'Grey Suit','medium','men',80,'Instock'),(27,'Grey Suit','large','men',80,'out of stock'),(28,'Grey Suit','extra large','men',80,'Instock'),(29,'White t-shirt','small','men',20,'Instock'),(30,'White t-shirt','medium','men',20,'Instock'),(31,'White t-shirt','large','men',20,'Instock'),(32,'White t-shirt','extra large','men',20,'Instock'),(33,'Black suit with tie','small','men',100,'Instock'),(34,'Black suit with tie','medium','men',100,'Instock'),(35,'Black suit with tie','large','men',100,'Instock'),(36,'Black suit with tie','extra large','men',100,'Instock'),(37,'Blue t-shirt','small','men',15,'Instock'),(38,'Blue t-shirt','medium','men',15,'Instock'),(39,'Blue t-shirt','large','men',15,'Instock'),(40,'Blue t-shirt','extra large','men',15,'Instock'),(41,'Black Party gown','small','women',80,'Instock'),(42,'Black Party gown','medium','women',80,'Instock'),(43,'Black Party gown','large','women',80,'Instock'),(44,'Black Party gown','extra large','women',80,'Instock'),(45,'Pink checks frock','small','girl',20,'Instock'),(46,'Pink checks frock','medium','girl',20,'Instock'),(47,'Pink checks frock','large','girl',20,'Instock'),(48,'Pink checks frock','extra large','girl',20,'out of stock'),(49,'blue t-shirt','small','boy',10,'Instock'),(50,'blue t-shirt','medium','boy',10,'Instock'),(51,'blue t-shirt','large','boy',10,'Instock'),(52,'blue t-shirt','extra large','boy',10,'Instock');
/*!40000 ALTER TABLE `dress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_summury`
--

DROP TABLE IF EXISTS `order_summury`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_summury` (
  `OrderID` int NOT NULL,
  `User_Name` varchar(45) NOT NULL,
  `Total_Price` int NOT NULL,
  PRIMARY KEY (`OrderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_summury`
--

LOCK TABLES `order_summury` WRITE;
/*!40000 ALTER TABLE `order_summury` DISABLE KEYS */;
INSERT INTO `order_summury` VALUES (25,'XYZ',80),(30,'ABC',65),(42,'PQR',40);
/*!40000 ALTER TABLE `order_summury` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordertable`
--

DROP TABLE IF EXISTS `ordertable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordertable` (
  `OrderID` int NOT NULL,
  `DressID` int NOT NULL,
  `Quantity` int NOT NULL,
  `TotalPrice` int NOT NULL,
  PRIMARY KEY (`OrderID`,`DressID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordertable`
--

LOCK TABLES `ordertable` WRITE;
/*!40000 ALTER TABLE `ordertable` DISABLE KEYS */;
INSERT INTO `ordertable` VALUES (25,26,1,80),(30,11,1,50),(30,20,1,15),(42,15,2,40);
/*!40000 ALTER TABLE `ordertable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trackingtable`
--

DROP TABLE IF EXISTS `trackingtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trackingtable` (
  `OrderID` int NOT NULL,
  `Status` varchar(45) NOT NULL,
  PRIMARY KEY (`OrderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trackingtable`
--

LOCK TABLES `trackingtable` WRITE;
/*!40000 ALTER TABLE `trackingtable` DISABLE KEYS */;
INSERT INTO `trackingtable` VALUES (25,'delivered'),(30,'in transit'),(42,'delivered');
/*!40000 ALTER TABLE `trackingtable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'cartcompanion'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-20 11:38:41

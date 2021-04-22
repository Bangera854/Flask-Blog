-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: troz
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `s_no` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `content` text NOT NULL,
  `date` date NOT NULL,
  `slug` varchar(45) DEFAULT NULL,
  `img_file` varchar(45) DEFAULT NULL,
  `tag_line` tinytext,
  PRIMARY KEY (`s_no`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'Paloma ','1 ounce Tequila,\r\n1 ounce grapefruit soda or grapefruit juice with sparkling water,\r\nFresh lime juice, combine tequila and lime juice in a highball glass with ice and a salted rim. \r\nAdd grapefruit soda and garnish with a grapefruit slice','2021-03-24','first-post','splash-bg','Quick Tequila recipe'),(2,'Food Recipe','Ingredients :\r\n8 cups tortilla chips\r\n1/2 cup Shredded mild cheddar cheese\r\n1/2 cup sliced fresh jalapeno peppers\r\n2.25oz sliced black olives drained\r\n1/2 cup TACO BELL Thick & Chunky medium salsa\r\n\r\nSteps:\r\nHeat oven to 400F\r\nLayer 1/3 each of the chips, cheese and peppers in shallow ovenproof dish. Repeat layers twice\r\nBake 7 min or until cheese is melted\r\nTop with remaining ingredients.','2021-04-12','second-post','img.jpg','Quick Nachos Recipe'),(3,'Damn','None','2021-03-21','third-post','img.png','third post'),(13,'Na','Nananana','2021-03-22','rata-post','img.png','Stu stu stu');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-22 12:02:48

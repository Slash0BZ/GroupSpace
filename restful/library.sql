-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room` (
  `rid` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `lid` int(11) NOT NULL,
  `occupancy` int(11) NOT NULL,
  `eid` varchar(256) NOT NULL,
  `noise` int(11) NOT NULL,
  `position` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (0,'UGL_Group_Room_1',1,8,'0',1,''),(1,'UGL_Group_Room_2',1,8,'0',2,''),(2,'UGL_Group_Room_3',1,8,'1',3,''),(3,'UGL_Group_Room_4',1,8,'1',2,''),(4,'UGL_Group_Room_5',1,4,'1',5,''),(5,'UGL_Group_Room_6',1,4,'1',7,''),(6,'UGL_Group_Room_7',1,4,'1',2,''),(7,'UGL_Group_Room_8',1,4,'1',4,''),(8,'UGL_Group_Room_9',1,4,'1',6,''),(9,'UGL_Group_Room_10',1,4,'1',8,''),(10,'UGL_Group_Room_11',1,4,'1',1,''),(11,'Main_Group_Room_214',3,4,'null',3,''),(12,'Main_Group_Room_216',3,6,'null',7,''),(13,'Grainger_Group_Room_405',0,4,'1',5,'40.112456883061206,-88.22738036513329'),(14,'Grainger_Group_Room_407',0,4,'1',9,'40.11243226741585,-88.22738036513329'),(15,'Grainger_Group_Room_408',0,6,'0,1',6,'40.11243226741585,-88.22715103626251'),(16,'Grainger_Group_Room_409',0,4,'1',4,'40.11240867741403,-88.2273830473423'),(17,'Grainger_Group_Room_410',0,6,'0,1',6,'40.11241072871885,-88.22715505957603'),(18,'Grainger_Group_Room_411',0,4,'null',3,'40.112376882181216,-88.2273817062378'),(19,'Grainger_Group_Room_412',0,8,'1',7,'40.11234713824031,-88.22715371847153'),(20,'Grainger_Group_Room_413',0,8,'1',1,'40.11233995866639,-88.22738572955132'),(21,'Grainger_Group_Room_414',0,8,'1',5,'40.11231329167102,-88.22719261050224'),(22,'Grainger_Group_Room_415',0,8,'1',5,'40.112317394286364,-88.22734147310257'),(23,'Grainger_Lower_Room_040C',0,6,'1',4,'40.11238508740402,-88.22696194052696'),(24,'Grainger_Lower_Room_040D',0,6,'1',8,'40.112384061751214,-88.22676748037338'),(25,'ACES_Study_Room_301',2,8,'null',6,''),(26,'ACES_Study_Room_305',2,8,'null',7,''),(27,'ACES_Study_Room_309',2,8,'null',1,''),(28,'ACES_Study_Room_401',2,8,'null',8,''),(29,'ACES_Study_Room_405',2,8,'null',9,''),(30,'ACES_Study_Room_409',2,8,'null',5,''),(31,'SSHEL_Collaboration_Room_100G',4,4,'null',6,''),(32,'SSHEL_Collaboration_Room_100H',4,4,'null',7,'');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `username` varchar(256) NOT NULL,
  `time` varchar(256) NOT NULL,
  `duration` varchar(256) NOT NULL,
  `rid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES ('grshen2','12/7/2017 13:30','30 minutes',17);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `username` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('grshen2','123456qwerty');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-07 20:30:09

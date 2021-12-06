-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: native_irish_trees
-- ------------------------------------------------------
-- Server version	8.0.3-rc-log

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
-- Table structure for table `trees`
--

DROP TABLE IF EXISTS `trees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trees` (
  `id` int(11) NOT NULL,
  `english_name` varchar(255) DEFAULT NULL,
  `irish_name` varchar(255) DEFAULT NULL,
  `scientific_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trees`
--

LOCK TABLES `trees` WRITE;
/*!40000 ALTER TABLE `trees` DISABLE KEYS */;
INSERT INTO `trees` VALUES (1,'Alder','Fearnóg','Alnus glutinosa'),(2,'Arbutus (Strawberry Tree)','Caithne','Arbutus unedo'),(3,'Ash','Fuinseóg','Fraxinus excelsior'),(4,'Aspen','Crann creathach','Populus tremula'),(5,'Birch (Downy)','Beith chlúmhach','Betula pubescens'),(6,'Birch (Silver)','Beith gheal','Betula pendula'),(7,'Blackthorn - Shrub','Draighean','Prunus spinosa'),(8,'Bramble - Shrub','Dris','Rubus fructicosus'),(9,'Broom - Shrub','Giolcach sléibhe','Cytisus scoparius'),(10,'Buckthorn - Shrub (Alder)','Paide bréan','Frangula alnus'),(11,'Buckthorn - Shrub (Purging)','Paide bréan','Rhamnus cathartic'),(12,'Cherry (Bird)','Donnroisc','Prunus padus'),(13,'Cherry (Wild)','Gean – crann silíní fiáin','Prunus avium'),(14,'Crab Apple','Crann fia-úll','Malus sylvestris'),(15,'Dog Rose - Shrub','Feirdhris','Rosa canina'),(16,'Elder - Shrub','Tromán','Sambucus nigra'),(17,'Gorse - Shrub','Aiteann','Ulex europaeus & Ulex gallii'),(18,'Guelder Rose - Shrub','Caorchon','Viburnum opulus'),(19,'Hawthorn','Sceach gheal','Crataegus monogyna'),(20,'Hazel','Coll','Corylus avellana'),(21,'Holly','Cuilleann','Ilex aquifolium'),(22,'Honeysuckle - Shrub','Féithleann','Lonicera periclymenum'),(24,'Ivy - Shrub','Eidhneán','Hedera helix'),(25,'Juniper - Shrub','Aiteal','Juniperus communis'),(26,'Oak (Pedunculate)','Dair ghallda','Quercus robur'),(27,'Oak (Sessile)','Dair ghaelach','Quercus petraea'),(28,'Rowan/Mountain Ash','Caorthann','Sorbus aucuparia'),(29,'Scots Pine','Péine albanach','Pinus syvestris'),(30,'Spindle - Shrub','Feoras','Euonymous eoropaeus'),(31,'Whitebeam','Fionncholl','Sorbus spp.'),(32,'Willow','Saileach','Salix spp.'),(33,'Wych Elm','Leamhán sléibhe','Ulmus glabra'),(34,'Yew','Lúr','Taxus baccata');
/*!40000 ALTER TABLE `trees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-06 14:54:09

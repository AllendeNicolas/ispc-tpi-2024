-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: data_human´s
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `caracteristicaspuesto`
--

DROP TABLE IF EXISTS `caracteristicaspuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caracteristicaspuesto` (
  `Id_caractpuesto` varchar(45) NOT NULL,
  `Id_vacantes` varchar(45) NOT NULL,
  `Descripcion` varchar(700) NOT NULL,
  `Condicioncontratacion` varchar(40) NOT NULL,
  `Experiencia` varchar(200) NOT NULL,
  `Excluyente` varchar(200) NOT NULL,
  `Seconsidera` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Id_caractpuesto`),
  UNIQUE KEY `Id_caractpuesto_UNIQUE` (`Id_caractpuesto`),
  UNIQUE KEY `Id_vacantes_UNIQUE` (`Id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caracteristicaspuesto`
--

LOCK TABLES `caracteristicaspuesto` WRITE;
/*!40000 ALTER TABLE `caracteristicaspuesto` DISABLE KEYS */;
INSERT INTO `caracteristicaspuesto` VALUES ('30001','30001','Se solicita personal para cubrir puesto de Maestranza, se requiere ser mayor de 18 años, tener secundario completo y residir en la ciudad de Cordoba. Las tareas son de mantenimiento, orden y limpieza, de espacios comunes del edificio, recolección de basura y desinfección, entre otros.','Permanente','Sin experiencia previa','Ser mayor de Edad, Secundario completo, residir en la Ciudad de Cordoba','Conocimiento y manejo, de aspiradoras e hidrolavadoras.'),('30002','30002','Se solicita personal de limpieza de caracter urgente, para cubrir puestos en Shpping Nuevo Centro.','Temporal','Sin Experiencia','Ser Mayor de edad, Secundario Completo, Residir en la Ciudad de Cordoba o Zonas aledañas','Manejo de Hidro-lavadora'),('30003','30003','Se solicita personal de Maestranza, por la mañana, de 8 a 13 hs, para Hospital Ferreyra','Temporal','Sin Experiencia','Ser Mayor de edad, Secundario completo, residir en la ciudad de Cordoba','Cualquier conocimiento en uso de aspiradoras e Hidro-lavadoras.'),('30004','30004','Se solicita personal para cubrir puesto de Maestranza, tareas a realizar, mantenimieto y limpieza de sectores de jardín y galerías de importante edificio, ubicado en zona centro.','Temporal','Sin Experiencia','Ser Mayor de Edad, Secundario Completo, residir en zona centro','Cualquier conocimiento en plomeria, electricidad y cuidado de jardínes.'),('30005','30005','Se solicita personal para cubrir puesto de Maestranza, encargado de edificio. Tareas, Limpeiza de espacios comunes, recolección de basura, Informe de estado general de la unidad.','Permanente','Con Experiencia','Ser Mayor de Edad, Secundario complreto, residir en Ciudad de Córdoba, o localidad cercana, no mayor a los 20 Km.','Conocimientos en Plomería y Cerrajería'),('30006','30006','Se solicira personal para cubrir puesto de Maestranza, Jefe de sector. Tareas: gestionar los recursos, y elemento de limpieza que reciban desde central. Controlar el cumplimiento de las tareas de mantenimiento, orden y limpieza, de los demás empleados, en los establecimientos asignados. ','Permanente','Con Experiencia','Ser Mayor de de Edad, Secundario Completo, residir en la Cordoba Capital, o en zonas aledañas, buena presencia, capacidad para trabajar bajo presión.','Conocimintos en uso de Excel, Sistemas de Gestión de personal en general. '),('30007','30007','Se solicita Maestranza de caracter urgente','Permanente','Sin Experiencia','Mayor de edad, residir en Cordoba Capital','Buena presencia'),('30008','30008','Se solicita Personal Carniceria, para cubrir puesto en importante local en el Mercado Norte.','Permanente','Con Experiencia','Ser Mayor de Edad, Secundario Completo, Residir en la ciudad de Cordoba','Buen manejo de Herraminentas de trabajo.');
/*!40000 ALTER TABLE `caracteristicaspuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `Id_empresa` int NOT NULL,
  `Razonsocial` varchar(20) NOT NULL,
  `Cuit` varchar(20) NOT NULL,
  `Rubro` tinytext NOT NULL,
  `Ubicacion` varchar(100) NOT NULL,
  `Cantvacantes` int NOT NULL,
  `Id_vacantes` int NOT NULL,
  PRIMARY KEY (`Id_empresa`),
  UNIQUE KEY `Id_empresa_UNIQUE` (`Id_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (10001,'Clean is good','30256856256','Limpieza','Cordoba',5,30001),(10002,'Paul Mc Carne','30659875435','Carniceria','Cordoba',2,30002),(10003,'Jueguito','30256874196','Jugueteria','Cordoba',1,30003),(10004,'L cafe','30256874156','Cafeteria','Cordoba',3,30004),(10005,'Ayudin Cool','30269587459','Limpieza','Cordoba',3,30005),(10006,'Desinf-accion','30563982156','Limpieza','Cordoba',5,30006),(10007,'Limpia Door','30526912589','Limpieza','Cordoba',2,30007),(10008,'Aspira Dora','30569871059','Limpieza','Cordoba',3,30008),(10009,'A Todotrapo','30658714569','Limpieza','Cordoba',6,30009),(10010,'Limpiecito','30658971259','Limpieza','Cordoba',4,30010);
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formularioaspirante`
--

DROP TABLE IF EXISTS `formularioaspirante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formularioaspirante` (
  `Id_formulario` int NOT NULL,
  `Id_vacantes` int NOT NULL,
  `Id_postulante` int NOT NULL,
  `Puestodeseado` text,
  `Fechapostulacion` date DEFAULT NULL,
  PRIMARY KEY (`Id_formulario`),
  UNIQUE KEY `Id_FORMULARIO_UNIQUE` (`Id_formulario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formularioaspirante`
--

LOCK TABLES `formularioaspirante` WRITE;
/*!40000 ALTER TABLE `formularioaspirante` DISABLE KEYS */;
INSERT INTO `formularioaspirante` VALUES (50001,30001,1,'Maestranza','2024-06-09'),(50002,30002,2,'Maestranza','2024-06-09'),(50003,30003,3,'Maestranza','2024-06-09'),(50004,30004,10,'Maestranza','2024-06-11'),(50005,30005,13,'Maestranza','2024-06-10'),(50006,30006,14,'Maestranza','2024-05-16'),(50007,30007,19,'Maestranza','2024-05-28'),(50008,30008,15,'Carnicero','2024-04-30');
/*!40000 ALTER TABLE `formularioaspirante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nivelacademico`
--

DROP TABLE IF EXISTS `nivelacademico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nivelacademico` (
  `Id_estudios` int NOT NULL,
  `Id_postulante` int NOT NULL,
  `Secundarios` varchar(200) DEFAULT NULL,
  `Universitarios` varchar(200) DEFAULT NULL,
  `Otros` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Id_estudios`),
  UNIQUE KEY `Id_postulante_UNIQUE` (`Id_postulante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nivelacademico`
--

LOCK TABLES `nivelacademico` WRITE;
/*!40000 ALTER TABLE `nivelacademico` DISABLE KEYS */;
INSERT INTO `nivelacademico` VALUES (1,1,'Completo','No posee','No posee'),(2,2,'Completo','No posee','No posee'),(3,3,'Completo','No posee','No posee'),(10,10,'Completo','No posee','No posee'),(13,13,'Completo','Parciales','No posee'),(14,14,'Completo','Completo','No posee'),(15,15,'Completo','Parciales','No posee'),(19,19,'Completo','Completo','No posee');
/*!40000 ALTER TABLE `nivelacademico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postulante`
--

DROP TABLE IF EXISTS `postulante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postulante` (
  `id_postulante` int NOT NULL,
  `Dni` int DEFAULT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  `Fechanacimiento` date DEFAULT NULL,
  `Residencia` varchar(45) DEFAULT NULL,
  `Nivelacademico` varchar(45) DEFAULT NULL,
  `C.v` varchar(45) DEFAULT NULL,
  `Puestodeseado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_postulante`),
  UNIQUE KEY `id_POSTULANTE_UNIQUE` (`id_postulante`),
  UNIQUE KEY `D.N.I_UNIQUE` (`Dni`),
  KEY `FK_Residencia_idx` (`Residencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postulante`
--

LOCK TABLES `postulante` WRITE;
/*!40000 ALTER TABLE `postulante` DISABLE KEYS */;
INSERT INTO `postulante` VALUES (1,35871057,'Nicolas','Allende','1992-05-06','Cordoba','Universitarios','Cargado','Maestranza'),(2,36692589,'Carlos','Aguirre','1991-02-07','Cordoba','Secundarios','Cargado','Maestranza'),(3,26892569,'Malena','Polanco','1996-10-04','Cordoba','Secundarios','Cargado','Maestranza'),(4,35986352,'Juliana','Salcedo','2000-09-06','Cordoba','Secundarios','Cargado','Vendedor'),(5,39685963,'Vittorio','Arjona','1998-01-26','Cordoba','Secundarios','Cargado','Operario'),(6,41968712,'Matias','Wider','1997-02-21','Cordoba','Secundarios','Cargado','Administrativo'),(7,31569825,'Esperanza','Castro','1996-05-23','Cordoba','Universitarios','Cargado','Vendedor'),(8,35953689,'Juan','Perez','1995-08-09','Cordoba','Universitarios','Cargado','Repositor'),(9,32966884,'Cecilia','Lopez','1993-07-10','Cordoba','Secundarios','Cargado','Vendedor'),(10,33989625,'Maura','Cuneo','1999-12-09','Salta','Secundarios','Cargado','Maestranza'),(11,33695852,'Alicia','Cataneo','2001-03-13','Tucuman','Universitarios','Cargado','Productor'),(12,32696874,'Pablo','Mateos','1992-10-10','Chaco','Secundarios','Cargado','Administrativo'),(13,40693542,'Damian','Cortez','1980-12-05','La Rioja','Secundarios','Cargado','Maestranza'),(14,39521558,'Martin','Joray','1985-12-12','Jujuy','Universitarios','Cargado','Maestranza'),(15,30569820,'Agustina','Sueldo','1993-10-12','Cordoba','Secundarios','Cargado','Carnicero'),(16,35876952,'Lucas','Sousa','1993-06-06','Neuquen','Universitarios','Cargado','Repositor'),(17,38967410,'Ernesto','Palomeque','1992-11-22','Chubut','Secundarios','Cargado','Guardia'),(18,26958741,'Monica','Llance','1995-07-15','Mendoza','Secundarios','Cargado','Vendedor'),(19,35986325,'Paula','Machuca','1996-03-25','Salta','Secundarios','Cargado','Maestranza'),(20,37852159,'Mauricio','Silva','1995-09-08','Catamarca','Universitarios','Cargado','Maestranza');
/*!40000 ALTER TABLE `postulante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puestodeseado`
--

DROP TABLE IF EXISTS `puestodeseado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puestodeseado` (
  `Titulopuesto` varchar(45) NOT NULL,
  `Rubro` varchar(100) NOT NULL,
  `Experiencia` varchar(300) NOT NULL,
  `Disponibilidadhoraria` varchar(100) NOT NULL,
  `Id_puestodeseado` varchar(45) NOT NULL,
  `Id_postulante` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puestodeseado`
--

LOCK TABLES `puestodeseado` WRITE;
/*!40000 ALTER TABLE `puestodeseado` DISABLE KEYS */;
INSERT INTO `puestodeseado` VALUES ('','Comercio','Super Mercado \"Super Centro\"','Full time','',''),('','Limpieza','Esencial Waith','Full time','',''),('','Limpieza','Todo Clean','Full time','','');
/*!40000 ALTER TABLE `puestodeseado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `residencia`
--

DROP TABLE IF EXISTS `residencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `residencia` (
  `Id_residencia` varchar(45) NOT NULL,
  `Id_postulante` varchar(45) NOT NULL,
  `Provincia` varchar(20) DEFAULT NULL,
  `Localidad` varchar(45) DEFAULT NULL,
  `Domicilio` varchar(45) DEFAULT NULL,
  `País` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id_residencia`),
  UNIQUE KEY `Id_postulante_UNIQUE` (`Id_postulante`),
  UNIQUE KEY `Id_residencia_UNIQUE` (`Id_residencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residencia`
--

LOCK TABLES `residencia` WRITE;
/*!40000 ALTER TABLE `residencia` DISABLE KEYS */;
INSERT INTO `residencia` VALUES ('1','1','Cordoba','Capital','Rioja 635','Argentina'),('10','10','Salta','Capital','9 de Julio','Argentina'),('13','13','La Rioja','Capital','San Martin 202','Argentina'),('14','14','Jujuy','Capital','Belgrano 562','Argentina'),('15','15','Cordoba','Capital','Corrientes 566','Argentina'),('19','19','Salta','Capital','Ituzaingo 599','Argentina'),('2','2','Cordoba','Capital','Indepndecia 252','Argentina'),('3','3','Cordoba','Capital','Buenos Aire 412','Argentina');
/*!40000 ALTER TABLE `residencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacantes`
--

DROP TABLE IF EXISTS `vacantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacantes` (
  `Id_vacantes` int NOT NULL,
  `Id_empresa` int NOT NULL,
  `Cantvacantes` int NOT NULL,
  `Titulopuesto` tinytext NOT NULL,
  `Id_caractpuesto` varchar(45) NOT NULL,
  `Fechavacantes` date NOT NULL,
  `Id_formulario` int NOT NULL,
  PRIMARY KEY (`Id_vacantes`),
  UNIQUE KEY `Id_VACANTE/S_UNIQUE` (`Id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacantes`
--

LOCK TABLES `vacantes` WRITE;
/*!40000 ALTER TABLE `vacantes` DISABLE KEYS */;
INSERT INTO `vacantes` VALUES (30001,10001,5,'Maestranza','30001','2024-06-09',50001),(30002,10005,3,'Maestranza','30002','2024-06-07',50002),(30003,10006,5,'Maestranza','30003','2024-06-03',50003),(30004,10007,2,'Maestranza','30004','2024-06-01',50004),(30005,10008,3,'Maestranza','30005','2024-06-01',50005),(30006,10009,6,'Maestranza','30006','2024-05-03',50006),(30007,10010,4,'Maestranza','30007','2024-05-06',50007),(30008,10002,2,'Carnicero','30008','2024-04-29',50008);
/*!40000 ALTER TABLE `vacantes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-14  0:08:08

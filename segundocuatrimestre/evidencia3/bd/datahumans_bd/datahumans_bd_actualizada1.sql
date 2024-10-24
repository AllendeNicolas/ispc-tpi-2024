-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: datahumans_prueba
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
  `id_caractpuesto` int NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `condicioncontratacion` varchar(45) NOT NULL,
  `excluyente` varchar(200) NOT NULL,
  `experiencia` varchar(250) NOT NULL,
  `seconsidera` varchar(250) NOT NULL,
  `id_vacantes` int NOT NULL,
  PRIMARY KEY (`id_caractpuesto`),
  KEY `fk_caractpuestovacante_idx` (`id_vacantes`),
  CONSTRAINT `fk_caractpuestovacante` FOREIGN KEY (`id_vacantes`) REFERENCES `vacantes` (`id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caracteristicaspuesto`
--

LOCK TABLES `caracteristicaspuesto` WRITE;
/*!40000 ALTER TABLE `caracteristicaspuesto` DISABLE KEYS */;
INSERT INTO `caracteristicaspuesto` VALUES (30001,'Se solicita personal  para cubrir puesto de maestranza, en Mercado Norte','Permanente','Mayor de edad, Secundario Completo, Residir en Cordoba.','Sin experiencia previa','-',30001),(30002,'Se solicita personal de limpieza urgente para cubrir pueto en empresa Grido','Temporal','Mayor de edad, secundario completo, residir en Cordoa','Sin experiencia','-',30002),(30003,'Se solicita personal de Maestranza por la mañana, para cubrir puesto en empresa Movistar','Temporal','Mayor de edad, secundario completo, residir en Cordoba','Sin experiencia','-',30003),(30004,'Se solicita personal para cubrir puesto de maestranza, en empresa Coca cola','Temporal','Mayor de edad, secundario completo, residir en Cordoba','Sin experiencia','-',30004),(30005,'Se solicita personal de Maestranza por la mañana, para cubrir puesto en empresa Personal','Permanente','Mayor de edad, secundario completo, residir en Cordoba','Sin experiencia','-',30005);
/*!40000 ALTER TABLE `caracteristicaspuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `id_empresa` int NOT NULL,
  `cuit` varchar(20) NOT NULL,
  `razonsocial` varchar(60) NOT NULL,
  `rubro` varchar(60) NOT NULL,
  `ubicacion` varchar(60) NOT NULL,
  `cantvacantes` int NOT NULL,
  `id_vacantes` int NOT NULL,
  PRIMARY KEY (`id_empresa`),
  UNIQUE KEY `cuit_UNIQUE` (`cuit`),
  UNIQUE KEY `id_empresa_UNIQUE` (`id_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (10001,'30-22569823-2','Clean is Good','Limpieza','Cordoba',5,30001),(10002,'30-12564258-6','Ayudin Cool','Limpieza','Cordoba',6,30002),(10003,'30-25487216-5','Limpia Door','Limpieza','Cordoba',6,30003),(10004,'30-25498723-5','Paul Mc Carne','Carniceria','Cordoba',2,30004),(10005,'30-25647112-6','A Todo Trapo','Limpieza','Cordoba',3,30005);
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formularioaspirante`
--

DROP TABLE IF EXISTS `formularioaspirante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formularioaspirante` (
  `id_formulario` int NOT NULL,
  `puestodeseado` varchar(100) NOT NULL,
  `fechapostulacion` date NOT NULL,
  `id_vacantes` int NOT NULL,
  `id_postulante` int NOT NULL,
  PRIMARY KEY (`id_formulario`),
  UNIQUE KEY `id_formulario_UNIQUE` (`id_formulario`),
  KEY `fk_postulanteformulario_idx` (`id_postulante`),
  KEY `vacante_idx` (`id_vacantes`),
  CONSTRAINT `fk_postulanteformulario` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_vacanteformulario` FOREIGN KEY (`id_vacantes`) REFERENCES `vacantes` (`id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formularioaspirante`
--

LOCK TABLES `formularioaspirante` WRITE;
/*!40000 ALTER TABLE `formularioaspirante` DISABLE KEYS */;
INSERT INTO `formularioaspirante` VALUES (50001,'Maestranza','2024-05-08',30001,1),(50002,'Maestranza','2024-01-25',30002,2),(50003,'Maestranza','2024-03-05',30003,3),(50004,'Carnicero','2024-02-26',30004,4);
/*!40000 ALTER TABLE `formularioaspirante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nivelacademico`
--

DROP TABLE IF EXISTS `nivelacademico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nivelacademico` (
  `id_nivelacademico` int NOT NULL,
  `id_universitarios` int NOT NULL,
  `id_secundarios` int NOT NULL,
  `id_otrosestudios` int NOT NULL,
  `id_postulante` int NOT NULL,
  PRIMARY KEY (`id_nivelacademico`),
  UNIQUE KEY `id_nivelacademico_UNIQUE` (`id_nivelacademico`),
  KEY `fk_postulante_idx` (`id_postulante`),
  CONSTRAINT `fk_postulantenivelacademico` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nivelacademico`
--

LOCK TABLES `nivelacademico` WRITE;
/*!40000 ALTER TABLE `nivelacademico` DISABLE KEYS */;
INSERT INTO `nivelacademico` VALUES (1,1,1,1,1),(2,2,2,2,2),(3,3,3,3,3),(4,4,4,4,4),(5,5,5,5,5),(6,6,6,6,6),(7,7,7,7,7),(8,8,8,8,8),(9,9,9,9,9),(10,10,10,10,10);
/*!40000 ALTER TABLE `nivelacademico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `otrosestudios`
--

DROP TABLE IF EXISTS `otrosestudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `otrosestudios` (
  `id_otrosestudios` int NOT NULL,
  `tiene otros estudios` varchar(20) NOT NULL,
  `establecimiento` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `estudios` varchar(45) DEFAULT NULL,
  `titulo` varchar(45) DEFAULT NULL,
  `fechafinalizacion` varchar(45) DEFAULT NULL,
  `id_nivelacademico` int NOT NULL,
  PRIMARY KEY (`id_otrosestudios`),
  KEY `fk_nivelacademicootrosest_idx` (`id_nivelacademico`),
  CONSTRAINT `fk_nivelacademicootrosest` FOREIGN KEY (`id_nivelacademico`) REFERENCES `nivelacademico` (`id_nivelacademico`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `otrosestudios`
--

LOCK TABLES `otrosestudios` WRITE;
/*!40000 ALTER TABLE `otrosestudios` DISABLE KEYS */;
INSERT INTO `otrosestudios` VALUES (1,'No','S/D','S/D','S/D','S/D','NO','S/D',1),(2,'No','S/D','S/D','S/D','S/D','NO','S/D',2),(3,'Si','UNCA','Cordoba','Argentina','Reparación de Aires Acondicionados','Tecnico en reparacion de aires acondicionados','2015-02-25',3),(4,'No','S/D','S/D','S/D','S/D','NO','S/D',4),(5,'Si','UNC','Cordoba','Argentina','Reparacion de bombas de agua','Tecnico en reparacion de bombas de piletas','2020-10-23',5),(6,'No','S/D','S/D','S/D','S/D','NO','S/D',6),(7,'Si','Inatituto Noa','Cordoba','Argentina','Secretariado Administrativo','Secretariado y administracion de cuentas','2021-06-09',7),(8,'No','S/D','S/D','S/D','S/D','S/D','S/D',8),(9,'No','S/D','S/D','S/D','S/D','S/D','S/D',9),(10,'Si','UNC','Cordoba','Argentina','Electricista','Electricista Matriculado','2021-06-22',10);
/*!40000 ALTER TABLE `otrosestudios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postulante`
--

DROP TABLE IF EXISTS `postulante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postulante` (
  `id_postulante` int NOT NULL,
  `dni` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `fechanacimiento` date NOT NULL,
  `curriculumvitae` varchar(250) NOT NULL,
  `id_residencia` int NOT NULL,
  `id_nivelacademico` int NOT NULL,
  `id_puestodeseado` int NOT NULL,
  `id_formulario` int NOT NULL,
  `id_usuario` int NOT NULL,
  PRIMARY KEY (`id_postulante`),
  UNIQUE KEY `id_postulante_UNIQUE` (`id_postulante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postulante`
--

LOCK TABLES `postulante` WRITE;
/*!40000 ALTER TABLE `postulante` DISABLE KEYS */;
INSERT INTO `postulante` VALUES (1,35871057,'Nicolas','Allende','1992-05-06','Cargado',1,1,1,5001,1),(2,36692589,'Carlos','Aguirre','1991-02-07','Cargado',2,2,2,5002,2),(3,26892569,'Malena','Polanco','1996-10-04','Cargado',3,3,3,5003,3),(4,35986352,'Juliana','Salcedo','2000-09-06','Cargado',4,4,4,5004,4),(5,39685963,'Vittorio','Arjona','1998-01-26','Cargado',5,5,5,5005,5),(6,41968712,'Matias','Wider','1997-02-21','Cargado',6,6,6,5006,6),(7,31569825,'Esperanza','Castro','1996-05-23','Cargado',7,7,7,5007,7),(8,35953689,'Juan','Perez','1995-08-09','Cargado',8,8,8,5008,8),(9,32966884,'Cecilia','Lopez','1993-07-10','Cargado',9,9,9,5009,9),(10,33989625,'Maura','Cuneo','1999-12-09','Cargado',10,10,10,5010,10);
/*!40000 ALTER TABLE `postulante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puestodeseado`
--

DROP TABLE IF EXISTS `puestodeseado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puestodeseado` (
  `id_puestodeseado` int NOT NULL,
  `titulopuesto` varchar(45) NOT NULL,
  `rubro` varchar(45) NOT NULL,
  `experiencia` varchar(250) NOT NULL,
  `disponibilidadhoraria` varchar(45) NOT NULL,
  `id_postulante` int NOT NULL,
  PRIMARY KEY (`id_puestodeseado`),
  UNIQUE KEY `id_puestodeseado_UNIQUE` (`id_puestodeseado`),
  KEY `fk_postulantepuestodeseado_idx` (`id_postulante`),
  CONSTRAINT `fk_postulantepuestodeseado` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puestodeseado`
--

LOCK TABLES `puestodeseado` WRITE;
/*!40000 ALTER TABLE `puestodeseado` DISABLE KEYS */;
INSERT INTO `puestodeseado` VALUES (1,'Maestranza','Limpieza','3 años en área de limpieza de la empresa Coca Cola','Part Time',1),(2,'Maestranza','Limpieza','1 año en área de limpieza en empresa Clean master, en Patio Olmos','Part Time',2),(3,'Maestranza','Limpieza','2 años, Encargada área de limpieza del Mercado Norte','Full Time',3),(4,'Vendedor','Atención al Cliente','3 años, atención al público, en heladeria Caseratto','Full Time',4),(5,'Cajero','Cobranzas','1 año, cajero en supermercado Bunos Dias','Full Time',5),(6,'Diseñador','Diseño','2 años, Diseñador de indumentaria deportiva','Full Time',6),(7,'Contador','Contabilidad','3 años, Contador Publico, administración de consircios','Full Time',7),(8,'Maestranza','Limpieza','Sin Experiencia','Part Time',8),(9,'Administrativo','Administracion','4 años, Secretaria de bufet de abogados \"El Cuervo te encuentra\" y tesorería del bufet.','Full Time',9),(10,'Modista','Reparación Textil','5 años, Encargada de Sector de costuras, en Fabrica de Indumentaria, \"Todo Jean´s\".','Full Time',10);
/*!40000 ALTER TABLE `puestodeseado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `residencia`
--

DROP TABLE IF EXISTS `residencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `residencia` (
  `id_residencia` int NOT NULL,
  `domicilio` varchar(60) NOT NULL,
  `localidad` varchar(45) NOT NULL,
  `provincia` varchar(45) NOT NULL,
  `país` varchar(45) NOT NULL,
  `id_postulante` int NOT NULL,
  PRIMARY KEY (`id_residencia`),
  UNIQUE KEY `id_residencia_UNIQUE` (`id_residencia`),
  KEY `fk_postulante_idx` (`id_postulante`),
  CONSTRAINT `fk_postulante` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residencia`
--

LOCK TABLES `residencia` WRITE;
/*!40000 ALTER TABLE `residencia` DISABLE KEYS */;
INSERT INTO `residencia` VALUES (1,'Buenos Aires 479, 3 C','Capital','Cordoba','Argentina',1),(2,'JuanAlverez 1256','Capital','Cordoba','Argentina',2),(3,'Rioja 56','Capital','Cordoba','Argentina',3),(4,'Chile 45','Capital','Cordoba','Argentina',4),(5,'Independencia 256, 4 B','Capital','Cordoba','Argentina',5),(6,'Ituzaingo 566','Capital','Cordoba','Argentina',6),(7,'Santiago Pinto 589','Capital','Cordoba','Argentina',7),(8,'Hirigoyen 587','San Fernando','Catamarca','Argentina',8),(9,'Maradona 96','San Miguel','Tucuman','Argentina',9),(10,'Boulevard Ilia 456, 11 C','Salto','Santa Fe','Argentina',10);
/*!40000 ALTER TABLE `residencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `secundarios`
--

DROP TABLE IF EXISTS `secundarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `secundarios` (
  `id_secundarios` int NOT NULL,
  `tiene estudios` varchar(20) NOT NULL,
  `colegio` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `especialidad` varchar(45) DEFAULT NULL,
  `titulo` varchar(45) DEFAULT NULL,
  `fechafinalizacion` varchar(45) DEFAULT NULL,
  `id_nivelacademico` int NOT NULL,
  PRIMARY KEY (`id_secundarios`),
  KEY `fk_nivelacademicoesecundarios_idx` (`id_nivelacademico`),
  CONSTRAINT `fk_nivelacademicoesecundarios` FOREIGN KEY (`id_nivelacademico`) REFERENCES `nivelacademico` (`id_nivelacademico`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secundarios`
--

LOCK TABLES `secundarios` WRITE;
/*!40000 ALTER TABLE `secundarios` DISABLE KEYS */;
INSERT INTO `secundarios` VALUES (1,'SI','Instituto Brizuela','Cordoba','Argentina','Gestion de las Organizaciones','Bachiller en Gestion Organizacional','2009-12-01',1),(2,'SI','IPEM 307','Cordoba','Argentina','Gestion Contable','Bachiller en contabilidad','2009-12-01',2),(3,'SI','Instiruto Sagrado Corazon','Cordoba','Argentina','Etica y Ciudadania','Espacialista en trabajo social','2013-12-01',3),(4,'SI','Instiruto San Jose','Cordoba','Argentina','Filosofia y sociologia','Tecnico en Sociologia Contemporanea','2020-12-01',4),(5,'SI','Colegio San Agustin','Cordoba','Argentina','Filosofia y sociologia','Tecnico en Sociologia Contemporanea','2015-12-01',5),(6,'SI','IPEM 300','Cordoba','Argentina','Administracion agropecuaria','Tecnico Agropecuario','2015-12-01',6),(7,'SI','SEDMA','Cordoba','Argentina','Administracion agropecuaria','Tecnico Agropecuario','2013-12-01',7),(8,'SI','Monserrat','Catamarca','Argentina','Ciencias Sociales','Tecnico en Ciencias sociales y Sociologia','2012-12-01',8),(9,'SI','Coronel Olmedo','Tucuman','Argentina','Gestion Contable','Bachiller en contabilidad','2010-12-01',9),(10,'SI','San Martín','Santa Fe','Argentina','Gestion de las Organizaciones','Bachiller en Gestion Organizacional','2019-12-01',10);
/*!40000 ALTER TABLE `secundarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `universitarios`
--

DROP TABLE IF EXISTS `universitarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `universitarios` (
  `id_universitarios` int NOT NULL,
  `tiene estudios` varchar(20) NOT NULL,
  `universidad` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `carrera` varchar(45) DEFAULT NULL,
  `titulo` varchar(45) DEFAULT NULL,
  `fechaegreso` varchar(45) DEFAULT NULL,
  `id_nivelacademico` int NOT NULL,
  PRIMARY KEY (`id_universitarios`),
  KEY `fk_nivelacademicoestudios_idx` (`id_nivelacademico`),
  CONSTRAINT `fk_nivelacademicoestudios` FOREIGN KEY (`id_nivelacademico`) REFERENCES `nivelacademico` (`id_nivelacademico`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `universitarios`
--

LOCK TABLES `universitarios` WRITE;
/*!40000 ALTER TABLE `universitarios` DISABLE KEYS */;
INSERT INTO `universitarios` VALUES (1,'SI','UNC','Cordoba','Argentina','Abogacia','Abogado','Sin Finalizar',1),(2,'SI','UNC','Cordoba','Argentina','Contabilidad','Contador','2016-12-01',2),(3,'NO','-','-','-','-','-','-',3),(4,'SI','UNC','Cordoba','Argentina','Odontologia','Odontologo','Sin Finalizar',4),(5,'NO','-','-','-','-','-','-',5),(6,'SI','UNC','Cordoba','Argentina','Agronomia','Ing. Agronomo','2022-12-01',6),(7,'SI','UNC','Cordoba','Argentina','Agronomia','Ing. Agronomo','2022-12-01',7),(8,'SI','UCA','Catamarca','Argentina','Filosofia','Filosofo','2022-12-01',8),(9,'NO','-','-','-','-','-','-',9),(10,'SI','UNC','Cordoba','Argentina','Medicina','Medico GEneral','Sin Finalizar',10);
/*!40000 ALTER TABLE `universitarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `dni` int NOT NULL,
  `correoelectronico` varchar(50) NOT NULL,
  `fechanacimiento` date NOT NULL,
  `nombreusuario` varchar(50) NOT NULL,
  `clave` varchar(200) NOT NULL,
  `id_postulante` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_postulanteusuario_idx` (`id_postulante`),
  CONSTRAINT `fk_postulanteusuario` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Nicolas','Allende',35871057,'nicoallende92@gmail.com','1992-05-06','Niquito92','0505NicoA*',1),(2,'Carlos','Aguirre',36692589,'carlitosag21@gmail.com','1991-02-07','Charlysims','125acrr++',2),(3,'Malena','Polanco',26892569,'maleloca@hotmail.com','1996-10-04','Malu55','5266MAl-',3),(4,'Juliana','Salcedo',35986352,'julisal@gmail.com','2000-09-06','Julibum21','2256JUJU+',4),(5,'Vittorio','Arjona',39685963,'vitto39@gmail.com','1998-01-26','Arjona52','53369ARJ++',5);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacantes`
--

DROP TABLE IF EXISTS `vacantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacantes` (
  `id_vacantes` int NOT NULL,
  `vacantesdisponibles` varchar(50) NOT NULL,
  `titulopuesto` varchar(45) NOT NULL,
  `fechavacantes` date NOT NULL,
  `id_empresa` int NOT NULL,
  `id_caractpuesto` int NOT NULL,
  `id_formulario` int NOT NULL,
  PRIMARY KEY (`id_vacantes`),
  KEY `fk_formulario_idx` (`id_formulario`),
  KEY `fk_vacante_empresa_idx` (`id_empresa`),
  CONSTRAINT `fk_vacante_empresa` FOREIGN KEY (`id_empresa`) REFERENCES `empresa` (`id_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacantes`
--

LOCK TABLES `vacantes` WRITE;
/*!40000 ALTER TABLE `vacantes` DISABLE KEYS */;
INSERT INTO `vacantes` VALUES (30001,'5','Maestranza','2024-05-06',10001,30001,50001),(30002,'6','Maestranza','2024-01-23',10002,30002,50002),(30003,'6','Maestranza','2024-03-02',10003,30003,50003),(30004,'2','Carniceria','2024-04-22',10003,30004,50004),(30005,'3','Maestranza','2024-07-15',10005,30005,50005);
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

-- Dump completed on 2024-10-23 22:05:54

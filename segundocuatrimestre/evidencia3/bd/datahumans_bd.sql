-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: data_human´s1
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
-- Table structure for table `puestodeseado`
--

DROP TABLE IF EXISTS `puestodeseado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puestodeseado` (
  `id_puestodeseado` int NOT NULL,
  `Titulopuesto` varchar(45) NOT NULL,
  `Rubro` varchar(45) NOT NULL,
  `Experiencia` varchar(200) NOT NULL,
  `Disponibilidadhoraria` varchar(200) NOT NULL,
  `id_postulante` int NOT NULL,
  PRIMARY KEY (`id_puestodeseado`),
  UNIQUE KEY `id_postulante_UNIQUE` (`id_postulante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `dni` varchar(15) NOT NULL,
  `correo_electronico` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `nombreUsuario` varchar(50) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `id_postulante` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dni` (`dni`),
  UNIQUE KEY `correo_electronico` (`correo_electronico`),
  UNIQUE KEY `nombreUsuario` (`nombreUsuario`),
  UNIQUE KEY `id_postulante_UNIQUE` (`id_postulante`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-06 15:14:09
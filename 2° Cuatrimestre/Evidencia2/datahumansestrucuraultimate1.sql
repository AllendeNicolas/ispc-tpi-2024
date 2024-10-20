-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: datahumans
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
  KEY `fk_vacantespuestos_idx` (`id_vacantes`),
  CONSTRAINT `fk_vacantespuestos` FOREIGN KEY (`id_vacantes`) REFERENCES `vacantes` (`id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `id_empresa` int NOT NULL,
  `cuit` int NOT NULL,
  `razonsocial` varchar(60) NOT NULL,
  `rubro` varchar(60) NOT NULL,
  `ubicacion` varchar(60) NOT NULL,
  `cantvacantes` int NOT NULL,
  `id_vacantes` int NOT NULL,
  PRIMARY KEY (`id_empresa`),
  UNIQUE KEY `cuit_UNIQUE` (`cuit`),
  KEY `fk_empresavacantes_idx` (`id_vacantes`),
  CONSTRAINT `fk_empresavacantes` FOREIGN KEY (`id_vacantes`) REFERENCES `vacantes` (`id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `fk_vacantes_idx` (`id_vacantes`),
  KEY `fk_postulanteformulario_idx` (`id_postulante`),
  CONSTRAINT `fk_postulanteformulario` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`),
  CONSTRAINT `fk_vacantes` FOREIGN KEY (`id_vacantes`) REFERENCES `vacantes` (`id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `fk_universitarios_idx` (`id_universitarios`),
  KEY `fk_secundarios_idx` (`id_secundarios`),
  KEY `fk_otrosestudios_idx` (`id_otrosestudios`),
  KEY `fk_postulante_idx` (`id_postulante`),
  CONSTRAINT `fk_otrosestudios` FOREIGN KEY (`id_otrosestudios`) REFERENCES `otrosestudios` (`id_otrosestudios`),
  CONSTRAINT `fk_postulantenivelacademico` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`),
  CONSTRAINT `fk_secundarios` FOREIGN KEY (`id_secundarios`) REFERENCES `secundarios` (`id_secundarios`),
  CONSTRAINT `fk_universitarios` FOREIGN KEY (`id_universitarios`) REFERENCES `universitarios` (`id_universitarios`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `otrosestudios`
--

DROP TABLE IF EXISTS `otrosestudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `otrosestudios` (
  `id_otrosestudios` int NOT NULL,
  `establecimiento` varchar(45) NOT NULL,
  `provincia` varchar(45) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `estudios` varchar(45) NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `fechafinalizacion` date NOT NULL,
  `id_nivelacademico` int NOT NULL,
  PRIMARY KEY (`id_otrosestudios`),
  KEY `fk_nivelacademicootrosest_idx` (`id_nivelacademico`),
  CONSTRAINT `fk_nivelacademicootrosest` FOREIGN KEY (`id_nivelacademico`) REFERENCES `nivelacademico` (`id_nivelacademico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

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
  UNIQUE KEY `Dni_UNIQUE` (`dni`),
  UNIQUE KEY `id_postulante_UNIQUE` (`id_postulante`),
  KEY `fk_residencia_idx` (`id_residencia`),
  KEY `fk_nivelacademico_idx` (`id_nivelacademico`),
  KEY `fk_puestodeseado_idx` (`id_puestodeseado`),
  KEY `fk_formulario_idx` (`id_formulario`),
  KEY `fk_usuario_idx` (`id_usuario`),
  CONSTRAINT `fk_formulario` FOREIGN KEY (`id_formulario`) REFERENCES `formularioaspirante` (`id_formulario`),
  CONSTRAINT `fk_nivelacademico` FOREIGN KEY (`id_nivelacademico`) REFERENCES `nivelacademico` (`id_nivelacademico`),
  CONSTRAINT `fk_puestodeseado` FOREIGN KEY (`id_puestodeseado`) REFERENCES `puestodeseado` (`id_puestodeseado`),
  CONSTRAINT `fk_residencia` FOREIGN KEY (`id_residencia`) REFERENCES `residencia` (`id_residencia`),
  CONSTRAINT `fk_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
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
  `titulopuesto` varchar(45) NOT NULL,
  `rubro` varchar(45) NOT NULL,
  `experiencia` varchar(250) NOT NULL,
  `disponibilidadhoraria` varchar(45) NOT NULL,
  `id_postulante` int NOT NULL,
  PRIMARY KEY (`id_puestodeseado`),
  KEY `fk_postulantepuestodeseado_idx` (`id_postulante`),
  CONSTRAINT `fk_postulantepuestodeseado` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `fk_postulante_idx` (`id_postulante`),
  CONSTRAINT `fk_postulante` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `secundarios`
--

DROP TABLE IF EXISTS `secundarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `secundarios` (
  `id_secundarios` int NOT NULL,
  `colegio` varchar(45) NOT NULL,
  `provincia` varchar(45) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `especialidad` varchar(45) NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `fechafinalizacion` int NOT NULL,
  `id_nivelacademico` int NOT NULL,
  PRIMARY KEY (`id_secundarios`),
  KEY `fk_nivelacademicoesecundarios_idx` (`id_nivelacademico`),
  CONSTRAINT `fk_nivelacademicoesecundarios` FOREIGN KEY (`id_nivelacademico`) REFERENCES `nivelacademico` (`id_nivelacademico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `universitarios`
--

DROP TABLE IF EXISTS `universitarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `universitarios` (
  `id_universitarios` int NOT NULL,
  `universidad` varchar(45) NOT NULL,
  `provincia` varchar(45) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `carrera` varchar(45) NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `fechaegreso` date NOT NULL,
  `id_nivelacademico` int NOT NULL,
  PRIMARY KEY (`id_universitarios`),
  KEY `fk_nivelacademicoestudios_idx` (`id_nivelacademico`),
  CONSTRAINT `fk_nivelacademicoestudios` FOREIGN KEY (`id_nivelacademico`) REFERENCES `nivelacademico` (`id_nivelacademico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `fk_postulanteusuario_idx` (`id_postulante`),
  CONSTRAINT `fk_postulanteusuario` FOREIGN KEY (`id_postulante`) REFERENCES `postulante` (`id_postulante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vacantes`
--

DROP TABLE IF EXISTS `vacantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacantes` (
  `id_vacantes` int NOT NULL,
  `cantavacantes` int NOT NULL,
  `titulopuesto` varchar(45) NOT NULL,
  `fechavacantes` date NOT NULL,
  `id_empresa` int NOT NULL,
  `id_caractpuesto` int NOT NULL,
  `id_formulario` int NOT NULL,
  PRIMARY KEY (`id_vacantes`),
  KEY `fk_empresa_idx` (`id_empresa`),
  KEY `fk_caractpuestovacante_idx` (`id_caractpuesto`),
  KEY `fk_formulario_idx` (`id_formulario`),
  KEY `fk_formulariovacante_idx` (`id_formulario`),
  CONSTRAINT `fk_caractpuestovacante` FOREIGN KEY (`id_caractpuesto`) REFERENCES `caracteristicaspuesto` (`id_caractpuesto`),
  CONSTRAINT `fk_empresa` FOREIGN KEY (`id_empresa`) REFERENCES `empresa` (`id_empresa`),
  CONSTRAINT `fk_formulariovacante` FOREIGN KEY (`id_formulario`) REFERENCES `formularioaspirante` (`id_formulario`)
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

-- Dump completed on 2024-10-19 22:16:46

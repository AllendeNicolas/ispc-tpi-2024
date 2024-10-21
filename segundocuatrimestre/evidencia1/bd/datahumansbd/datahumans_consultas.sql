insert into caracteristicaspuesto (Id_caractpuesto, Id_vacantes, Descripcion, Condicioncontratacion, Experiencia, Excluyente, Seconsidera)
values ('31007, '30007, 'Se solicita Maestranza de caracter urgente', 'Permanente', 'Sin Experiencia',
'Mayor de edad, residir en Cordoba Capital', 'Buena presencia');

Select * from postulantes;

Select empresa.Razonsocial, empresa.Rubro, empresa.Cuit from empresa;

Select * from empresa where Cantvacantes >= 3 and Cantvacantes <= 10;

Select * from postulante where residencia = 'Cordoba' limit 5;

Select * from postulante
where postulante.Fechanacimiento between "1991-02-07" and "1944-02-27";

Select empresa.Id_empresa, empresa.Razonsocial, empresa.Rubro, vacantes.Titulopuesto, vacantes.Cantvacantes, vacantes.Fechavacantes
From empresa
INNER JOIN vacantes ON empresa.Id_empresa = vacantes.Id_empresa

-- Crear el esquema
CREATE SCHEMA IF NOT EXISTS `data_human´s` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `data_human´s`;

-- Crear la tabla vacantes
CREATE TABLE IF NOT EXISTS `data_human´s`.`vacantes` (
  `Id_vacantes` INT NOT NULL,
  `Id_empresa` INT NOT NULL,
  `Cantvacantes` INT NOT NULL,
  `Titulopuesto` TINYTEXT NOT NULL,
  `Id_caractpuesto` VARCHAR(45) NOT NULL,
  `Fechavacantes` DATE NOT NULL,
  `Id_formulario` INT NOT NULL,
  PRIMARY KEY (`Id_vacantes`),
  UNIQUE INDEX `Id_VACANTE/S_UNIQUE` (`Id_vacantes` ASC) VISIBLE,
  UNIQUE INDEX `Id_FORMULARIO_UNIQUE` (`Id_formulario` ASC) VISIBLE
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- Crear la tabla caracteristicaspuesto
CREATE TABLE IF NOT EXISTS `data_human´s`.`caracteristicaspuesto` (
  `Id_caractpuesto` VARCHAR(45) NOT NULL,
  `Id_vacantes` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(700) NOT NULL,
  `Condicion/contratacion` VARCHAR(40) NOT NULL,
  `Experiencia` VARCHAR(200) NOT NULL,
  `Excluyente` VARCHAR(200) NOT NULL,
  `Seconsidera` VARCHAR(200) NULL DEFAULT NULL,
  `vacantes_Id_vacantes` INT NOT NULL,
  PRIMARY KEY (`Id_caractpuesto`, `vacantes_Id_vacantes`),
  UNIQUE INDEX `Id_vacantes_UNIQUE` (`Id_vacantes` ASC) VISIBLE,
  INDEX `fk_caracteristicaspuesto_vacantes1_idx` (`vacantes_Id_vacantes` ASC) VISIBLE,
  CONSTRAINT `fk_caracteristicaspuesto_vacantes1`
    FOREIGN KEY (`vacantes_Id_vacantes`)
    REFERENCES `data_human´s`.`vacantes` (`Id_vacantes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- Crear la tabla empresa
CREATE TABLE IF NOT EXISTS `data_human´s`.`empresa` (
  `Id_empresa` INT NOT NULL,
  `Razonsocial` VARCHAR(20) NOT NULL,
  `Cuit` VARCHAR(20) NOT NULL,
  `Rubro` TINYTEXT NOT NULL,
  `Ubicacion` VARCHAR(100) NOT NULL,
  `Cantvacantes` INT NOT NULL,
  `Id_vacantes` INT NOT NULL,
  `vacantes_Id_vacantes` INT NOT NULL,
  PRIMARY KEY (`Id_empresa`, `vacantes_Id_vacantes`),
  UNIQUE INDEX `Id_EMPRESA_UNIQUE` (`Id_empresa` ASC) VISIBLE,
  UNIQUE INDEX `Id_VACANTES_UNIQUE` (`Id_vacantes` ASC) VISIBLE,
  INDEX `fk_empresa_vacantes1_idx` (`vacantes_Id_vacantes` ASC) VISIBLE,
  CONSTRAINT `fk_empresa_vacantes1`
    FOREIGN KEY (`vacantes_Id_vacantes`)
    REFERENCES `data_human´s`.`vacantes` (`Id_vacantes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- Crear la tabla postulante
CREATE TABLE IF NOT EXISTS `data_human´s`.`postulante` (
  `id_postulante` INT NOT NULL,
  `Dni` INT NULL DEFAULT NULL,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Apellido` VARCHAR(45) NULL DEFAULT NULL,
  `Fechanacimiento` DATE NULL DEFAULT NULL,
  `Residencia` VARCHAR(45) NULL DEFAULT NULL,
  `Nivelacademico` VARCHAR(45) NULL DEFAULT NULL,
  `C.v` VARCHAR(45) NULL DEFAULT NULL,
  `Puestodeseado` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_postulante`),
  UNIQUE INDEX `id_POSTULANTE_UNIQUE` (`id_postulante` ASC) VISIBLE,
  UNIQUE INDEX `D.N.I_UNIQUE` (`Dni` ASC) VISIBLE,
  INDEX `FK_Residencia_idx` (`Residencia` ASC) VISIBLE
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- Crear la tabla formularioaspirante
CREATE TABLE IF NOT EXISTS `data_human´s`.`formularioaspirante` (
  `Id_formulario` INT NOT NULL,
  `Id_vacantes` INT NOT NULL,
  `Id_postulante` INT NOT NULL,
  `Puestodeseado` TEXT NULL DEFAULT NULL,
  `Fechapostulacion` DATE NULL DEFAULT NULL,
  `postulante_id_postulante` INT NOT NULL,
  `vacantes_Id_vacantes` INT NOT NULL,
  PRIMARY KEY (`Id_formulario`, `postulante_id_postulante`, `vacantes_Id_vacantes`),
  UNIQUE INDEX `Id_FORMULARIO_UNIQUE` (`Id_formulario` ASC) VISIBLE,
  INDEX `fk_formularioaspirante_postulante_idx` (`postulante_id_postulante` ASC) VISIBLE,
  INDEX `fk_formularioaspirante_vacantes1_idx` (`vacantes_Id_vacantes` ASC) VISIBLE,
  CONSTRAINT `fk_formularioaspirante_postulante`
    FOREIGN KEY (`postulante_id_postulante`)
    REFERENCES `data_human´s`.`postulante` (`id_postulante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_formularioaspirante_vacantes1`
    FOREIGN KEY (`vacantes_Id_vacantes`)
    REFERENCES `data_human´s`.`vacantes` (`Id_vacantes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- Crear la tabla nivelacademico
CREATE TABLE IF NOT EXISTS `data_human´s`.`nivelacademico` (
  `Id_estudios` INT NOT NULL,
  `Id_postulante` INT NOT NULL,
  `Secundarios` VARCHAR(200) NULL DEFAULT NULL,
  `Universitarios` VARCHAR(200) NULL DEFAULT NULL,
  `Otros` VARCHAR(200) NULL DEFAULT NULL,
  `postulante_id_postulante` INT NOT NULL,
  PRIMARY KEY (`Id_estudios`, `postulante_id_postulante`),
  UNIQUE INDEX `Id_postulante_UNIQUE` (`Id_postulante` ASC) VISIBLE,
  INDEX `fk_nivelacademico_postulante1_idx` (`postulante_id_postulante` ASC) VISIBLE,
  CONSTRAINT `fk_nivelacademico_postulante1`
    FOREIGN KEY (`postulante_id_postulante`)
    REFERENCES `data_human´s`.`postulante` (`id_postulante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- Crear la tabla postulante_has_postulante
CREATE TABLE IF NOT EXISTS `data_human´s`.`postulante_has_postulante` (
  `postulante_id_postulante` INT NOT NULL,
  `postulante_id_postulante1` INT NOT NULL,
  PRIMARY KEY (`postulante_id_postulante`, `postulante_id_postulante1`),
  INDEX `fk_postulante_has_postulante_postulante2_idx` (`postulante_id_postulante1` ASC) VISIBLE,
  INDEX `fk_postulante_has_postulante_postulante1_idx` (`postulante_id_postulante` ASC) VISIBLE,
  CONSTRAINT `fk_postulante_has_postulante_postulante1`
    FOREIGN KEY (`postulante_id_postulante`)
    REFERENCES `data_human´s`.`postulante` (`id_postulante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_postulante_has_postulante_postulante2`
    FOREIGN KEY (`postulante_id_postulante1`)
    REFERENCES `data_human´s`.`postulante` (`id_postulante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-- Crear la tabla puestodeseado
CREATE TABLE IF NOT EXISTS `data_human´s`.`puestodeseado` (
  `Titulopuesto` VARCHAR(45) NOT NULL,
  `Rubro` VARCHAR(100) NOT NULL,
  `Experiencia` VARCHAR(300) NOT NULL,
  `Disponibilidadhoraria` VARCHAR(100) NOT NULL,
  `Id_puestodeseado` VARCHAR(45) NOT NULL,
  `Id_postulante` VARCHAR

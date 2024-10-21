-- Modificaciones a la tabla `caracteristicaspuesto`
ALTER TABLE caracteristicaspuesto
MODIFY COLUMN Id_caractpuesto INT NOT NULL,
MODIFY COLUMN Id_vacantes INT NOT NULL,
MODIFY COLUMN Descripcion VARCHAR(500) NOT NULL,
MODIFY COLUMN Condicioncontratacion VARCHAR(255) NOT NULL,
MODIFY COLUMN Experiencia VARCHAR(255) NOT NULL;

-- Modificaciones a la tabla `empresa`
ALTER TABLE empresa
DROP COLUMN Id_vacantes;

-- Modificaciones a la tabla `formularioaspirante`
ALTER TABLE formularioaspirante
MODIFY COLUMN Puestodeseado INT,
ADD CONSTRAINT fk_puestodeseado FOREIGN KEY (Puestodeseado) REFERENCES puestodeseado(Id_puestodeseado);

-- Modificaciones a la tabla `nivelacademico`

CREATE TABLE secundarios (
    Id_secundario INT PRIMARY KEY,
    Id_postulante INT,
    NombreInstitucion VARCHAR(255),
    CONSTRAINT fk_postulante_secundarios FOREIGN KEY (Id_postulante) REFERENCES postulante(id_postulante)
);

CREATE TABLE universitarios (
    Id_universitario INT PRIMARY KEY,
    Id_postulante INT,
    NombreInstitucion VARCHAR(255),
    CONSTRAINT fk_postulante_universitarios FOREIGN KEY (Id_postulante) REFERENCES postulante(id_postulante)
);

CREATE TABLE otros (
    Id_otros INT PRIMARY KEY,
    Id_postulante INT,
    Descripcion VARCHAR(255),
    CONSTRAINT fk_postulante_otros FOREIGN KEY (Id_postulante) REFERENCES postulante(id_postulante)
);

DROP TABLE nivelacademico;

-- Modificaciones a la tabla `postulante`
ALTER TABLE postulante
RENAME COLUMN `C.v` TO `CV`;

-- Modificaciones a la tabla `puestodeseado`
ALTER TABLE puestodeseado
DROP INDEX id_postulante;

-- Modificaciones a la tabla `residencia`
ALTER TABLE residencia
DROP INDEX Id_postulante_UNIQUE,
ADD CONSTRAINT fk_postulante_residencia FOREIGN KEY (Id_postulante) REFERENCES postulante(id_postulante);

-- Modificaciones a la tabla `usuarios`
ALTER TABLE usuarios
ADD CONSTRAINT fk_postulante_usuarios FOREIGN KEY (id_postulante) REFERENCES postulante(id_postulante);

-- Modificaciones a la tabla `vacantes`
ALTER TABLE vacantes
MODIFY COLUMN Titulopuesto VARCHAR(255) NOT NULL,
ADD CONSTRAINT fk_empresa_vacantes FOREIGN KEY (Id_empresa) REFERENCES empresa(Id_empresa);

INSERT INTO caracteristicaspuesto (id_caractpuesto, descripcion, condicioncontratacion, excluyente, experiencia, seconsidera, id_vacantes)
VALUES (31007,
'Se solicita Maestranza de caracter urgente',
'Permanente',
'Mayor de edad, residir en Cordoba Capital',
'Sin Experiencia',
'Buena presencia', 
31007);

INSERT INTO postulante (id_postulante, dni, nombre, apellido, fechanacimiento, curriculumvitae, id_residencia, id_nivelacademico, id_puestodeseado, id_formulario, id_usuario)
VALUES (11,
356368952,
'Norma',
'Castro',
'2000-12-03',
'cargado', 
11,
11,
11,
50005,
6);

UPDATE empresa 
SET cantvacantes = 8 
WHERE id_empresa = 10001;

SELECT * FROM postulante;

SELECT * FROM empresa 
WHERE cantvacantes BETWEEN 3 AND 10;

SELECT * FROM postulante 
INNER JOIN residencia ON postulante.id_postulante = residencia.id_postulante
WHERE residencia.localidad = 'Cordoba'
LIMIT 5;

SELECT * FROM postulante
WHERE postulante.Fechanacimiento BETWEEN '1944-02-27' AND '1991-02-07';

SELECT empresa.id_empresa, empresa.razonsocial, empresa.rubro, vacantes.titulopuesto, vacantes.vacantesdisponibles, vacantes.fechavacantes
FROM empresa
INNER JOIN vacantes ON empresa.id_empresa = vacantes.id_empresa;

SELECT * 
FROM postulante
INNER JOIN puestodeseado
ON postulante.id_puestodeseado = puestodeseado.id_puestodeseado;

SELECT postulante.nombre, postulante.apellido, postulante.dni, puestodeseado.titulopuesto
FROM postulante
LEFT JOIN puestodeseado 
ON postulante.id_postulante = puestodeseado.id_postulante;

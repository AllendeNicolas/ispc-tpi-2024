INSERT INTO caracteristicaspuesto (Id_caractpuesto, Id_vacantes, Descripcion, Condicioncontratacion, Experiencia, Excluyente, Seconsidera)
VALUES (31007, 
30007,
'Se solicita Maestranza de caracter urgente',
'Permanente',
'Sin Experiencia',
'Mayor de edad, residir en Cordoba Capital',
'Buena presencia');

UPDATE empresa 
SET Cantvacantes = 8 
WHERE Id_empresa = 10001;

SELECT * FROM postulante;

SELECT * FROM empresa 
WHERE Cantvacantes BETWEEN 3 AND 10;

SELECT * FROM postulante 
INNER JOIN residencia ON postulante.Id_postulante = residencia.Id_postulante
WHERE residencia.Localidad = 'Cordoba'
LIMIT 5;

SELECT * FROM postulante
WHERE postulante.Fechanacimiento BETWEEN '1944-02-27' AND '1991-02-07';

SELECT empresa.Id_empresa, empresa.Razonsocial, empresa.Rubro, vacantes.Titulopuesto, vacantes.Cantvacantes, vacantes.Fechavacantes
FROM empresa
INNER JOIN vacantes ON empresa.Id_empresa = vacantes.Id_empresa;

SELECT postulante.Nombre, postulante.Apellido, postulante.Dni, puestodeseado.Titulopuesto
FROM postulante 
LEFT JOIN puestodeseado ON postulante.id_postulante = puestodeseado.id_postulante;

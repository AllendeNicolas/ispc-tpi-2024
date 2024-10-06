SELECT Nombre, Puestodeseado
FROM postulante
LEFT JOIN puestodeseado
ON postulante.Nombre = puestodeseado.Titulopuesto;


def conectar_base_datos():
    
    print("""CONEXIÓN Y TESTEO DE LA BASE DE DATOS\n
          INGRESA LOS DATOS DE TU SERVIDOR LOCAL  (EL PUERTO TIENE EL VALOR 3306 POR DEFAULT)""")
    usuario = str(input('User:'))
    contrasena = str(input('Password:'))

    import mysql.connector
    postulantes_cba = None
    conexion = mysql.connector.connect(user=usuario,
                                    password=contrasena,
                                    host='localhost',
                                    database="datahumans_prueba"
                                    )

    cursor = conexion.cursor()




    cursor.execute("""INSERT INTO caracteristicaspuesto (id_caractpuesto, descripcion, condicioncontratacion, excluyente, experiencia, seconsidera, id_vacantes)
                      VALUES (31007,'Se solicita Maestranza de caracter urgente','Permanente','Mayor de edad, residir en Cordoba Capital','Sin Experiencia','Buena presencia', 31007)""")

    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("""INSERT INTO caracteristicaspuesto (id_caractpuesto, descripcion, condicioncontratacion, excluyente, experiencia, seconsidera, id_vacantes)
            VALUES (31007,'Se solicita Maestranza de caracter urgente','Permanente','Mayor de edad, residir en Cordoba Capital','Sin Experiencia','Buena presencia', 31007)""")


    cursor.execute('''UPDATE empresa 
                      SET cantvacantes = 8 
                      WHERE id_empresa = 10001''')
    
    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("""UPDATE empresa 
             SET cantvacantes = 8 
             WHERE id_empresa = 10001""")


    cursor.execute('SELECT * FROM postulante')

    resultado = cursor.fetchall()

    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("SELECT * FROM postulante")

    print('RESULTADO DE LA CONSULTA:')
    
    for i in resultado:
        print(i)

    cursor.execute('SELECT * FROM empresa WHERE cantvacantes BETWEEN 3 AND 10')

    resultado = cursor.fetchall()

    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print('SELECT * FROM empresa WHERE cantvacantes BETWEEN 3 AND 10')

    print('RESULTADO DE LA CONSULTA:')
    
    for i in resultado:
        print(i)

    cursor.execute("""SELECT * FROM postulante 
                      INNER JOIN residencia ON postulante.id_postulante = residencia.id_postulante
                      WHERE residencia.localidad = 'Cordoba'
                     LIMIT 5""")
    
    resultado = cursor.fetchall()

    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("""SELECT * FROM postulante 
             INNER JOIN residencia ON postulante.id_postulante = residencia.id_postulante
             WHERE residencia.localidad = 'Cordoba'
             LIMIT 5""")

    print('RESULTADO DE LA CONSULTA:')
    
    for i in resultado:
        print(i)
    
    cursor.execute("""SELECT * FROM postulante
                      WHERE postulante.Fechanacimiento BETWEEN '1944-02-27' AND '1991-02-07'""")
    
    resultado = cursor.fetchall()
    
    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("""SELECT * FROM postulante
            WHERE postulante.Fechanacimiento BETWEEN '1944-02-27' AND '1991-02-07'""")

    print('RESULTADO DE LA CONSULTA:')
    
    for i in resultado:
        print(i)


    cursor.execute("""SELECT empresa.id_empresa, empresa.razonsocial, empresa.rubro, vacantes.titulopuesto, vacantes.vacantesdisponibles, vacantes.fechavacantes
                      FROM empresa
                      INNER JOIN vacantes ON empresa.id_empresa = vacantes.id_empresa""")
    
    resultado = cursor.fetchall()
    
    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("""SELECT empresa.id_empresa, empresa.razonsocial, empresa.rubro, vacantes.titulopuesto, vacantes.vacantesdisponibles, vacantes.fechavacantes
            FROM empresa
            INNER JOIN vacantes ON empresa.id_empresa = vacantes.id_empresa""")

    print('RESULTADO DE LA CONSULTA:')
    
    for i in resultado:
        print(i)

    cursor.execute("""SELECT * 
                      FROM postulante
                      INNER JOIN puestodeseado
                      ON postulante.id_puestodeseado = puestodeseado.id_puestodeseado""")
    
    resultado = cursor.fetchall()
    
    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("""SELECT * 
            FROM postulante
            INNER JOIN puestodeseado
            ON postulante.id_puestodeseado = puestodeseado.id_puestodeseado""")

    print('RESULTADO DE LA CONSULTA:')
    
    for i in resultado:
        print(i)

    cursor.execute("""SELECT postulante.nombre, postulante.apellido, postulante.dni, puestodeseado.titulopuesto
                      FROM postulante
                      LEFT JOIN puestodeseado 
                      ON postulante.id_postulante = puestodeseado.id_postulante""")
    
    resultado = cursor.fetchall()
    
    print('-' * 70)
    print('SE EJECUTÓ LA SIGUIENTE CONSULTA:\n')
    print("""SELECT postulante.nombre, postulante.apellido, postulante.dni, puestodeseado.titulopuesto
            FROM postulante
            LEFT JOIN puestodeseado 
            ON postulante.id_postulante = puestodeseado.id_postulante""")

    print('RESULTADO DE LA CONSULTA:')
    
    for i in resultado:
        print(i)












    conexion.close()

conectar_base_datos()
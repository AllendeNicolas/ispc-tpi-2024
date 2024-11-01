import mysql.connector

# Función para gestionar la base de datos
def gestionar_base_datos(conexion, cursor):
    while True:
        print("\n1. Ejecutar consulta UPDATE, Ingrese nueva cantidad de Vacantes")
        print("2. Ejecutar consulta SELECT")
        print("3. Ejecutar consulta INSERT, Inserte un Nuevo Postulante")
        print("4. Volver al menú anterior")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                variable = int(input("Cantidad de Vacantes que desea cargar: "))
                cursor.execute(f'''UPDATE empresa SET cantvacantes = {variable} WHERE id_empresa = 10001''')
                conexion.commit()
                print("La carga de Vacantes, se realizó con éxito")
            except ValueError:
                print("Por favor, ingrese un número entero.")
            except mysql.connector.Error as err:
                print(f"Ha habido un ERROR, revise la consulta, o los datos a cargar: {err}")

        elif opcion == '2':
            while True:
                print("\n1. Seleccionar Vacantes, entre 3 y 10 Disponibles")
                print("2. Seleccionar 5 postulantes que residan en Córdoba")
                print("3. Seleccionar Vacantes Disponibles de cada Empresa")
                print("4. Seleccionar Postulantes y su Puesto Deseado")
                print("5. Seleccionar todos los Postulantes")
                print("6. Volver al menú anterior")

                sub_opcion = input("Selecciona una opción: ")

                if sub_opcion == '1':
                    cursor.execute('SELECT * FROM empresa WHERE cantvacantes BETWEEN 3 AND 10')
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(i)

                elif sub_opcion == '2':
                    cursor.execute('''SELECT * FROM postulante
                                      INNER JOIN residencia ON postulante.id_postulante = residencia.id_postulante
                                      WHERE residencia.localidad = 'Cordoba'
                                      LIMIT 5''')
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(i)

                elif sub_opcion == '3':
                    cursor.execute('''SELECT empresa.id_empresa, empresa.razonsocial, empresa.rubro, vacantes.titulopuesto, vacantes.vacantesdisponibles, vacantes.fechavacantes
                                      FROM empresa
                                      INNER JOIN vacantes ON empresa.id_empresa = vacantes.id_empresa''')
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(i)

                elif sub_opcion == '4':
                    cursor.execute('''SELECT postulante.nombre, postulante.apellido, postulante.dni, puestodeseado.titulopuesto
                                      FROM postulante
                                      LEFT JOIN puestodeseado ON postulante.id_postulante = puestodeseado.id_postulante''')
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(i)

                elif sub_opcion == '5':
                    cursor.execute('''SELECT * FROM postulante''')
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(i)

                elif sub_opcion == '6':
                    break

                else:
                    print("Opción no válida, por favor intenta de nuevo.")

        elif opcion == '3':
            try:
                cursor.execute('''INSERT INTO postulante (id_postulante, dni, nombre, apellido, fechanacimiento, curriculumvitae, id_residencia, id_nivelacademico, id_puestodeseado, id_formulario, id_usuario)
                                  VALUES (11, 356368952, 'Norma', 'Castro', '2000-12-03', 'Cargado', 11, 11, 11, 50005, 6);''')
                conexion.commit()
                print("Inserción realizada con éxito.")
            except mysql.connector.Error as err:
                print(f"Ha habido un ERROR, revise la consulta, o los datos a cargar: {err}")

        elif opcion == '4':
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Función del menú principal
def conectar_base_datos():
    print("CONEXIÓN Y TESTEO DE LA BASE DE DATOS\n")
    usuario = input('User:')
    contrasena = input('Password:')

    conexion = None
    try:
        conexion = mysql.connector.connect(user=usuario,
                                           password=contrasena,
                                           host='localhost',
                                           database="datahumans_probando")
        print("La Base de Datos se ha conectado con éxito.")
    except mysql.connector.Error as err:
        print(f"No se ha conectado a la Base de Datos, por favor, revise Usuario y contraseña, o si existe o no una Base de Datos: {err}")

    cursor = conexion.cursor() if conexion else None

    while True:
        print("\n1. Ir a la Gestión de Base de Datos")
        print("2. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            if cursor:
                gestionar_base_datos(conexion, cursor)
            else:
                print("No hay conexión, puede que las consultas realizadas, no se reflejen en la Base de Datos.")
                gestionar_base_datos_simulado()
        elif opcion == '2':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

    if cursor:
        cursor.close()
    if conexion:
        conexion.close()

def gestionar_base_datos_simulado():
    while True:
        print("\n1. Simular consulta UPDATE")
        print("2. Simular consulta SELECT")
        print("3. Simular consulta INSERT")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            variable = int(input("Cantidad de Vacantes que desea cargar: "))
            print(f"Simulación de actualización: UPDATE empresa SET cantvacantes = {variable} WHERE id_empresa = 10001")
            print("Se ha actualizado correctamente (simulación).")
        
        elif opcion == '2':
            print("Simulación de ejecución de consultas SELECT:")
            print("1. SELECT * FROM empresa WHERE cantvacantes BETWEEN 3 AND 10")
            print("2. SELECT * FROM postulante INNER JOIN residencia ON postulante.id_postulante = residencia.id_postulante WHERE residencia.localidad = 'Cordoba' LIMIT 5")
            print("3. SELECT empresa.id_empresa, empresa.razonsocial, empresa.rubro, vacantes.titulopuesto, vacantes.vacantesdisponibles, vacantes.fechavacantes FROM empresa INNER JOIN vacantes ON empresa.id_empresa = vacantes.id_empresa")
            print("4. SELECT postulante.nombre, postulante.apellido, postulante.dni, puestodeseado.titulopuesto FROM postulante LEFT JOIN puestodeseado ON postulante.id_postulante = puestodeseado.id_postulante")
            print("5. SELECT * FROM postulante")

        elif opcion == '3':
            print("Simulación de inserción de un nuevo postulante:")
            print("INSERT INTO postulante (id_postulante, dni, nombre, apellido, fechanacimiento, curriculumvitae, id_residencia, id_nivelacademico, id_puestodeseado, id_formulario, id_usuario) VALUES (11, 356368952, 'Norma', 'Castro', '2000-12-03', 'Cargado', 11, 11, 11, 50005, 6);")
            print("Inserción realizada con éxito (simulación).")

        elif opcion == '4':
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    conectar_base_datos()

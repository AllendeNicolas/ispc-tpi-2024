#Importamos MySQL connector (para interactuar con bases de datos de MySQL)

import mysql.connector

#FUNCION PARA GESTIONAR LA BASE DE DATOS: Esta función se encarga de gestionar las operaciones de base de datos. Presenta un submenú con opciones para ejecutar diferentes consultas SQL o volver al menú principal.

# Cree Sub-menús, de acuerdo a la consulta SQL

# Ejecución de Consultas UPDDATE: Esta opción ejecuta una consulta UPDATE que actualiza el número de vacantes en la tabla empresa para una empresa específica.

def gestionar_base_datos(cursor):
    while True:
        print("\n1. Ejecutar consulta UPDATE, Ingrese nueva cantidad de Vacantes")
        print("2. Ejecutar consulta SELECT")
        print("3. Ejecutar consulta INSERT, Inserte un Nuevo Postulante")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            
          variable = int(input("Cantidad de Vacantes que desea cargar: ")) 
          cursor.execute (f'''UPDATE empresa SET cantvacantes = {variable} 
                         WHERE id_empresa = 10001''')
          print("La carga de Vacantes, se realizó con éxito")
           
 #Sub-menu para consultas SELECT: Ejecución de consultas SELECT, cada una de estas opciones ejecuta una consulta SELECT diferente y muestra los resultados.
 
           
        elif opcion == '2':
            while True:
                print("\n1. Seleccionar Vacantes, entre 3 y 10 Disponibles ")
                print("2. Seleccionar 5 postulantes que residan en Córdoba")
                print("3. Seleccionar Vacantes Disponibles de cada Empresa")
                print("4. Seleccionar Postulantes y su Puesto Deseado")
                print("5 Seleccionar todos los Postulantes")
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
                
                elif sub_opcion == '3':
                    cursor.execute('''INSERT INTO postulante (id_postulante, dni, nombre, apellido, fechanacimiento, curriculumvitae, id_residencia, id_nivelacademico, id_puestodeseado, id_formulario, id_usuario)
                                      VALUES (11, 356368952, 'Norma', 'Castro', '2000-12-03', 'Cargado', 11, 11, 11, 50005, 6);''')
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(i)     
                else:
                    print("Opción no válida, por favor intenta de nuevo.")
                
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

#FUNCION DEL MENU PRINCIPAL:Esta opción gestiona el menú principal del programa. Aquí se puede elegir entre gestionar la base de datos, volver al menú principal, o salir de la aplicación. Esta función establece una conexión a la base de datos, crea un cursor y pasa el control a la función gestionar_base_datos cuando se selecciona la opción correspondiente.

def conectar_base_datos():
    
    print("CONEXIÓN Y TESTEO DE LA BASE DE DATOS\n")
    usuario = str(input('User:'))
    contrasena = str(input('Password:'))

    import mysql.connector
    postulantes_cba = None
    conexion = mysql.connector.connect(user=usuario,
                                    password=contrasena,
                                    host='localhost',
                                    database="basededatosaconectar"
                                    )

    cursor = conexion.cursor()

    while True:
        print("\n1. Ir a la Gestión de Base de Datos")
        print("2. Volver al Menú Principal")
    
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            gestionar_base_datos(cursor)
        elif opcion == '2':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

    cursor.close()
    conexion.close()

if __name__ == "__main__":
    conectar_base_datos()

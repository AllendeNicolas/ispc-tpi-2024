import mysql.connector
from getpass import getpass  # no se puede ver la contrasenia
import re #validaciones de contra y usuario
import captcha #validación con CAPTCHA

# Conectar a la base de datos
connection = mysql.connector.connect(user='root',
                                    password='root',
                                    port='3306',
                                    host='localhost',
                                    database="datahumans_db"
                                    )
cursor = connection.cursor()

# Función para validar la contraseña
def validar_clave(clave):
    if len(clave) < 8:
        return False
    if not re.search(r"[a-z]", clave):  # Al menos una minúscula
        return False
    if not re.search(r"[A-Z]", clave):  # Al menos una mayúscula
        return False
    if not re.search(r"[0-9]", clave):  # Al menos un número
        return False
    if not re.search(r"[\W_]", clave):  # Al menos un carácter especial
        return False
    return True

# Función de verificación con captcha
def verificacion():

    if captcha.verificar_captcha():
        try:
            connection.commit()
            print("Usuario registrado con éxito.")
        except mysql.connector.Error as err:
            print(f"Error: {err}") 
            connection.rollback()
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            connection.rollback()
    else:
        print("Algo está mal, inténtalo nuevamente")
        verificacion()

# Función para registrar un usuario
def registrar_usuario():
    print("Por favor, ingrese los siguientes datos del usuario:")

        # Validar DNI único
    while True:
        dni = input("DNI: ")
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE dni = %s", (dni,))
        if cursor.fetchone()[0] > 0:
            print("Error: Este DNI ya está registrado. Inténtalo de nuevo.")
        else:
            break
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo_electronico = input("Correo Electrónico: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
        # Validar nombre de usuario
    while True:
        nombreUsuario = input("Nombre de Usuario (6-12 caracteres): ")
        if len(nombreUsuario) < 6 or len(nombreUsuario) > 12:
            print("Error: El nombre de usuario debe tener entre 6 y 12 caracteres.")
            continue

        # Verificar si el nombre de usuario ya existe
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nombreUsuario = %s", (nombreUsuario,))
        if cursor.fetchone()[0] > 0:
            print("Error: El nombre de usuario ya está en uso. Intenta con otro.")
        else:
            break

    # Validar clave
    while True:
        clave = getpass("Clave (mínimo 8 caracteres, incluyendo 1 minúscula, 1 mayúscula, 1 número y 1 carácter especial): ")
        if not validar_clave(clave):
            print("Error: La contraseña no cumple con los requisitos de seguridad.")
        else:
            break


    # Comando SQL para insertar los datos en la tabla 'usuarios'
    sql = """
    INSERT INTO usuarios (nombre, apellido, dni, correo_electronico, fecha_nacimiento, nombreUsuario, clave)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    # Ejecutar la consulta con los valores proporcionados
    cursor.execute(sql, (nombre, apellido, dni, correo_electronico, fecha_nacimiento, nombreUsuario, clave))

    #verificar usuario con captcha
    verificacion()


# Llamar a la función para registrar el usuario
registrar_usuario()

# Cerrar la conexión
cursor.close()
connection.close()

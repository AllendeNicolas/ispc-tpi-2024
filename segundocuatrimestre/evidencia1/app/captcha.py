import aritmetica
import random

"""
Importamos random para definir números aleatorios
y generamos la operación aritmética utilizando
funciones aleatorias del módulo aritmetica.py
Además guardamos el operador matemático
correspondiente a la operación ejecutada
"""

operaciones = [aritmetica.sumar, aritmetica.restar, aritmetica.dividir, aritmetica.multiplicar]
operacion = random.choice(operaciones)
num1 = round(random.uniform(1, 10), 0)
num2 = round(random.uniform(1, 10), 0)
resultado = operacion(num1, num2)

if operacion == aritmetica.sumar:
    operador = "+"

elif operacion == aritmetica.restar:
    operador = "-"

elif operacion == aritmetica.dividir:
    operador = "/"

elif operacion == aritmetica.multiplicar:
    operador = "*"

"""
Mostramos al usuario la operación y le solicitamos su respuesta
Luego verificamos si la respuesta es correcta:
En caso de serlo, se le otorga acceso
En caso de no serlo, se le pedirá que intente nuevamente
"""
def verificar_captcha():

    try:
        print(f"Resuelve la siguiente operación: {num1} {operador} {num2} = ?")
        respuesta = float(input("Ingresa tu respuesta (un número con dos decimales): "))
        print(f"Tu respuesta es: {respuesta}")
        if respuesta == resultado:
            print("¡Felicidades, Registro finalizado!")
            return True
        else:
            print("Respuesta incorrecta. Inténtalo de nuevo.")
            return False
    except:
        print("Algo salió mal, inténtalo de nuevo. Recuerda ingresar un número con dos decimales")


#La función "sumar" recibe dos números reales y devuelve la suma de los mismos
def sumar (a, b):
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

    return round(a+b, 2)

#La función "restar" recibe dos números reales y devuelve la resta del primero menos el segundo
def restar(a, b):
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

    return round(a-b, 2)

#La función "dividir" recibe dos números reales y devuelve el resultado de dividir el primer número por el segundo
def dividir(a, b):
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

    try:
        return round(a/b, 2)
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    except TypeError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

#La función "multiplicar" recibe dos números reales y devuelve la multiplicación de los mismos
def multiplicar(a, b):
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

    return round(a*b, 2)

#La función "sumar_n" recibe una cantidad variable (n) de números reales y devuelve la suma de los mismos
def sumar_n(*values):
    try:
        values=list(map(float, values))

        print(f'{values=}')

        return round(sum(values), 2)

    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

#La función "promedio_n" recibe una cantidad variable (n) de números reales y devuelve el valor promedio de los mismos
def promedio_n(*values):
    try:
        values=list(map(float, values))

        print(f'{values=}')

        return round(sum(values)/len(values), 2)

    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")
"""variables: us = nombre de usuario, pwd = contraseña. 
Estas variables serán comparadas con clave-valor en el diccionario cuando haya un registro de usuario"""

def login():
    print('                   Ingrese usuario y contraseña para ingresar al sistema')
    us = input("nombre de usuario ")
    pwd = input("contraseña ")

    k = 0 #variable para indicar al usuario que intente nuevamente si no hay coincidencia en el diccionario
    import f_registro 
    import reg_users from f_registro.registro() 

    '''nombre de archivos ficticios. Depende del desarrollo de la función de registrar usuario. 
    en la iteracion abajo, sucede los mismo'''

    for i in range(len(f_registro.reg_users)):
        if f_registro.reg_users[i].Nombre == us and f_registro.reg_users[i].Clave == pwd:
        print("Bienvenid@!")
        k = 1
        break

if k == 0:
    print("Usuario o clave incorrecta. Intente nuevamente!")

print("-----------------------")
print("1. Login")
print("2. Registrar usuario")
print("-----------------------")

opc = int(input("Ingrese una opcion: "))

if opc <1 or opc>2:
    print("Opción incorrecta. Ingrese nuevamente")
    
elif opc == 1:
    import login_sql
    login_sql.login()

elif opc == 2:
    import registro_usuario
    registro_usuario.registrar_usuario()

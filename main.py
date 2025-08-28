#Inicio de sesion con validacion de contraseña y de cuenta
import csv
import getpass
import bcrypt

especials = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

#Menu de inicio
def main():
    while True:
        print("\n --- Menú Principal ---")
        print("1.Iniciar sesion")
        print("2.Registrar usuario")
        print("3.Salir")
        respuesta = input("Qué deseas hacer?: ").strip().lower()
        if "iniciar" in respuesta or respuesta == "1":
            inicioSesUser()
        elif "registrar" in respuesta or respuesta == "2":
            registUsr()  
        elif "sal" in respuesta or respuesta == "3":
            salida()
            break
        else:
            print("Escoge una opción válida")

#Buscar al usuario en el archivo csv           
def buscar_usuario(userName):
    """
    Devuelve la lista con los datos del usuario si existe, o None si no está.
    """
    try:
        with open ("cuentasUsuarios.csv", mode="r", newline="", encoding="utf-8") as archivo:
            readUser = csv.reader(archivo)
            for linea in readUser:
                userList = linea [2]
                if userName in userList:
                    return linea
    except FileNotFoundError:
        print("El archivo de usuarios no existe todavía.")
    return None

#Verificar que la contraseña ingresada es la del usuario en bytes
def validarContraseñaBytes(userPasscode, passWordHashed):
    if bcrypt.checkpw(userPasscode.encode('utf-8'), passWordHashed):
        return True
    else:
        return False

#Inicio de sesion con usuario y contraseña
def inicioSesUser():
    intentFallidos = 3
    while intentFallidos > 0:
        print("\n ---Iniciar Sesión ---")
        userName = input("Ingrese su usuario: ")
        userPasscode = getpass.getpass("Ingrese su clave: ")

        usuarioDatos = buscar_usuario(userName)  # Devuelve la línea o None
        if usuarioDatos is None:
            intentFallidos -= 1
            print("Usuario no encontrado.")
        else:
            # El hash está guardado en la posición 3 (índice 3) según tu CSV
            passWordHashedStr = usuarioDatos[3]  
            passWordHashedBytes = passWordHashedStr.encode('utf-8')  # Convertir string a bytes

            passCode_es_valido = validarContraseñaBytes(userPasscode, passWordHashedBytes)

            if passCode_es_valido:
                print("Usuario y contraseña correctos.")
                sesionIniciadaUser()
                return
            else:
                intentFallidos -= 1
                print("Contraseña incorrecta.")

        if intentFallidos == 1:
            print("Haz intentado muchas veces. Tu cuenta se bloqueará si vuelves a ingresar mal tu contraseña")
        elif intentFallidos == 0:
            print("Número de intentos superado. Inténtalo después de 30 minutos.")

    
    #FUNCIONES DEL USUARIO
#Que puede hacer el usuario una vez iniciada sesio? 
def sesionIniciadaUser():
    print("\n ---Bienvenido---")
    print("  Menú  ")
    print("1.Cambiar de contraseña")
    print("2.salir")
    input("Qué deseas hacer?: ")


        #REGISTRO DEL USUARIO
#Validación del usuario
def validWritedUsername(userName):
            #Otra forma de resolverlo
            #return userName.isdigit() or userName[0].isdigit()
    if userName.isdigit():
        print("El nombe de usuario no puede ser numerico")
        return False
    if userName[0].isdigit():
        print("El nombre de usuario no puede empezar con números")
        return False
    return True

#Validar que el usuario exista
def validExistedUsername(userName):
    return buscar_usuario(userName) is not None
        
#Validar que la contraseña no tenga el nombre de la persona
def noNamePassword(passWord, realUserName):
    name_exists = False
    if realUserName.lower() in passWord.lower():
        name_exists = True
    return name_exists

#Validar que sea una contraseña segura
def validPassword(passWord):
    requisitos = []
    if len(passWord) < 8:
        requisitos.append("Debe de tener al menos 8 dígitos")

    #verificar que no haya espacios en la contraseña
    if " " in passWord:
        requisitos.append("La contraseña no puede tener espacios")

    if not any(char.isdigit() for char in passWord):
        requisitos.append("Debe de tener al menos un número")

    if not any(char.isupper() for char in passWord):
        requisitos.append("Debe de tener una letra en mayúscula")

    if not any(char in especials for char in passWord):
        requisitos.append("Debe contener al menos un carácter especial")
    return requisitos

#Encriptar contraseña del usuario
def encriptarContraseña(passWord):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passWord.encode('utf-8'), salt)
    return hashed

#Función para hacer el guardado de los datos del usuario
def guardarDatosUsuario(realUserName, realLastName, userName, passWordHashed, realBirthDay):
    with open ("cuentasUsuarios.csv", mode="a", newline="", encoding="utf-8") as archivo:
        readUser = csv.writer(archivo)
        readUser.writerow([realUserName, realLastName, userName, passWordHashed.decode('utf-8'), realBirthDay])
        print(f"Te has registrado exitosamente.")

#Crear el usuario y contraseña
def registUsr():
    print("\n ---Ingresa tus datos---")
    realUserName = input("Ingrese su nombre: ").capitalize()
    realLastName = input("Ingrese su apellido: ").capitalize()
    realBirthDay = input("Ingrese su fecha de cumpleaños (DD/MM/AAAA): ")
    while True:
        userName = input("Escriba su nombre de usuario: ")
        if not validWritedUsername(userName):
            continue
            #OTRA FORMA DE RESOLVER
            #if validWritedUsername(userName):
            #print("El usuario no debe ser solo numérico.")

        if validExistedUsername(userName):
            print("El usuario ya existe. Escribe uno nuevo")
        else:
            break
    while True:
        passWord = input("Ingrese su contraseña: ")
        if noNamePassword(passWord, realUserName):
            print("La contraseña no puede contener su nombre.")
            continue
        requisitos = validPassword(passWord)
        if requisitos:
            for error in requisitos:
                print(error)
            continue
        else:
            print("Contraseña válida")
            break  

#En si hace la encripcion de la contraseña
    passWordHashed = encriptarContraseña(passWord)
    guardarDatosUsuario(realUserName, realLastName, userName, passWordHashed, realBirthDay)

#Iniciar sesion con el usuario nuevo creado
    input("\n Presiona ENTER para iniciar sesión")
    inicioSesUser()

#Salida
def salida():
    print("Vuelve pronto")
main()
import getpass
def menu():
    print("Menu de Operaciones.")
    print("1. primera_operacion")
    print("2. segunda_operacion")
    print("3. tercera_operacion")
    print("4. cuarta_operacion")
    print("5. Salir")
    op = input ("Ingrese el numero de operacion que desee realizar: ")
    op = int(op)
    if op==1: primera_operacion()
    elif op==2: segunda_operacion()
    elif op==3: tercera_operacion()
    elif op==4: cuarta_operacion()
    elif op==5: 
        print ("")
        print ("que tenga buen dia o yo que se")
        exit()
    else: 
        print ("")
        print ("Error de Opcion se cerrara el programa")
        print ("por no leer bien las instrucciones")
        exit()
def primera_operacion():
    print ("")
    print ("Hacer division de 2 numeros, sin usar /,%")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    a=num1
    b=num2
    x=0
    while ( num1 >=  num2):
        num1=num1-num2
        x=x+1
    print ("el resto es: ", num1,"y ",a,"/",b,"=",x)
    print("")
    menu()   
def segunda_operacion():
    print("")
    print ("Hacer Divisores de un numero >99999999999999.")
    num1 = int(input("ingresa un numero mayor a 99999999999999: "))
    cont=0
    while ( num1 <= 99999999999999):
        num1 = int(input("ingresa un numero mayor a 99999999999999 por favor: "))
    for i in range (1,num1+1):
        if (num1//i==0):
            cont=cont +1
    print ("la cantidad de divisores de ",num1,"es", cont)
    print("")
    menu()
def tercera_operacion():
    print("")
    print ("Hacer Capicua.")
    menu()
def cuarta_operacion():
    print("")
    print ("Hacer Cambio de Base.")
    menu()

registrousuario = ("Miky","Archangel","Lab111")
registrocontraseña = ("nov2020","lab2020")
def sesion(usuario,contraseña):
    if usuario in registrousuario:
        if contraseña in registrocontraseña:
            return 1
        else:
            print("\n\tContraseña con coinciden...\n")
    else:
        return 2
usuario=input("USUARIO: ")
contraseña = getpass.getpass("CONTRASEÑA: ")
if sesion(usuario,contraseña)==1:
    print("BIENVENIDO  ",usuario)
    menu()
else:
    print("ERROR!!!!!!!, Usuario y Contrseña no registrados")


import getpass as pssd
import os


def menulogin():  # esta funcion me permite ver el menu principal
    print("**------WELCOME SYSTEM POS------**")
    while True:
        user = str(input(" *---INICIAR SESION---*\n"
                         "usuario: "))
        if user == "admin":
            while True:
                pasword = pssd.getpass('password: ')
                if pasword == '12345':
                    print("***SESION INICIADA.....***")
                    break
            break
        else:
            continue
    systema('borrar')
    menu_primary()


def menu_primary():
    print("")
    while True:
        option_menu = int(input(""
                                "1 - \n"
                                "2 - \n"
                                "3 - \n"
                                "4 - \n"
                                "5 - \n"
                                "6 - \n"
                                "7 - Salir\n"
                                "Seleccione: "))
        if option_menu == '1':
            print("")
        elif option_menu == '2':
            print("")
        elif option_menu == '3':
            print("")
        elif option_menu == '4':
            print("")
        elif option_menu == '5':
            print("")
        elif option_menu == '6':
            print("")
        elif option_menu == '7':
            if input("Seguro (s/n): ") == "s":
                break


def menu_almacen():
    print("___--Menu Almacen--___")
    while True:
        option_menu = int(input(""
                                "1 - Registrar un Producto nuevo\n"
                                "2 - Buscar Producto\n"
                                "3 - Modificar Producto\n"
                                "4 - Mostrar información Almacen\n"
                                "5 - Borrar un Producto\n"
                                "6 - Borrar todos los artículos\n"
                                "7 - Salir\n"
                                "Seleccione: "))
        if option_menu == '1':
            print("")
        elif option_menu == '2':
            print("")
        elif option_menu == '3':
            print("")
        elif option_menu == '4':
            print("")
        elif option_menu == '5':
            print("")
        elif option_menu == '6':
            print("")
        elif option_menu == '7':
            if input("Seguro (s/n): ") == "s":
                break


def systema(x):
    if x == 'borrar':
        if os.name == 'posix':
            return os.system('clear')
        else:
            return os.system('cls')
    elif x == 'sys':
        if os.name == 'posix':
            return print('UNIX')
        else:
            return print('windows')
    else:
        return print("Parametro invalido")

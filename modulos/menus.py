import getpass as pssd
import os
from modulos import clientes, alamacen


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
    print("___---Menu Principal---___")
    while True:
        option_menu = int(input(""
                                "1 - REALIZAR UNA VENTA\n"
                                "2 - CLIENTES\n"
                                "3 - ALMACEN\n"
                                "4 - BOLETAS\n"
                                "5 - Salir\n"
                                "Seleccione: "))
        if option_menu == 1:
            print("ventas!!")
            menu_ventas()
        elif option_menu == 2:
            print("CLIENTES!!")
        elif option_menu == 3:
            menu_almacen()
        elif option_menu == 4:
            print("BOLETAS!!")
        elif option_menu == 5:
            salir = str(input("Seguro (s/n): "))
            if salir == 's':
                break
            else:
                continue
        else:
            continue


def menu_ventas():
    print("___--Menu VENTAS--___")
    while True:
        print("")


def menu_clientes():
    print("___--Menu Clientes--___")
    clientes.init_cliente()


def menu_almacen():
    print("___--Menu Almacen--___")
    while True:
        option_menu = input(""
                            "1 - Registrar un Producto nuevo\n"
                            "2 - Buscar Producto\n"
                            "3 - Modificar Producto\n"
                            "4 - Mostrar información Almacen\n"
                            "5 - Borrar un Producto\n"
                            "6 - Borrar todos los artículos\n"
                            "7 - Salir\n"
                            "Seleccione: ")
        if option_menu == 1:
            print("Producto Registrado Exitosamente")
        elif option_menu == 2:
            print("Busqueda No encontrado")
        elif option_menu == 3:
            print("Producto Modificado Exitosamente")
        elif option_menu == 4:
            print("INFO Almacen")
        elif option_menu == 5:
            print("Producto borrado")
        elif option_menu == 6:
            print("Productos borrados Exitosamente")
        elif option_menu == 7:
            if input("Seguro (s/n): ") == "s":
                break
            else:
                continue
        else:
            continue


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

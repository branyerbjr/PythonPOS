import getpass as pssd
import os
from modulos import clientes, almacen, boletas


def menulogin(u):  # Funcion DE INICIO DE SESION
    print("**------WELCOME SYSTEM POS------**")
    while True:
        user = str(input(" *---INICIAR SESION---*\n"
                         "usuario: "))
        if user == u[0]:
            while True:
                pasword = pssd.getpass('password: ')
                if pasword == u[1]:
                    print("***SESION INICIADA.....***")
                    break
            break
        else:
            continue
    systema('borrar')
    menu_primary()


def menu_primary():
    systema('borrar')
    print("___---Menu Principal---___")
    while True:
        option_menu = int(input("¿Que desea Realizar?\n"
                                "1 - REALIZAR UNA VENTA\n"
                                "2 - CLIENTES\n"
                                "3 - ALMACEN\n"
                                "4 - BOLETAS\n"
                                "5 - Salir\n"
                                "Seleccione: "))
        if option_menu == 1:
            systema('borrar')
            menu_ventas()
        elif option_menu == 2:
            systema('borrar')
            menu_clientes()
        elif option_menu == 3:
            systema('borrar')
            menu_almacen()
        elif option_menu == 4:
            systema('borrar')
        elif option_menu == 5:
            salir = str(input("Seguro (s/n): "))
            if salir == 's':
                break
            else:
                continue
        else:
            continue


def menu_ventas():
    systema('borrar')
    while True:
        print("___--SYSTEM POS--___")
        boletas.boleta_venta(
            almacen.Selector_Productos(),
            clientes.Select_cliente())
        if str(input("¿Desea Regresar Menu principal? (s/n): ")) == 's':
            break
        else:
            continue
    menu_primary()


def menu_clientes():
    systema('borrar')
    while True:
        print("___--Menu Clientes--___")
        clientes.init_cliente()
        if str(input("¿Desea Regresar Menu principal? (s/n): ")) == 's':
            break
        else:
            continue
    menu_primary()


def menu_almacen():
    systema('borrar')
    print("___--Menu Almacen--___")
    almacen.ini_Productos()
    menu_primary()


def menu_boletas():
    if str(input("Desea ver Facturas(s/n)")) == 's':
        boletas.Ver_boletas()
    else:
        menu_primary()


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

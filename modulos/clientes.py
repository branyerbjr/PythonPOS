global  dic_clientes
dic_clientes= {}
def agregar_cliente():
    nombre = input("Ingrese su nombre: ")
    ruc = int(input("Ingrese su RUC: "))
    dic_clientes[nombre] = ruc
    print("Bienvenido(a)", nombre)
    print(dic_clientes) #solo lo puse para ver los cambios, lo borran


agregar_cliente()

def buscar_cliente():
    buscar = input("Ingrese el Nombre que desea buscar: ")
    if buscar in dic_clientes.keys():
        print("Nombre:", buscar, "-", "RUC:", dic_clientes[buscar])
    else:
        print("No se encontró el nombre ingresado, intente de nuevo.")


buscar_cliente()

def modificar_clientes():
    modificar = input("Ingrese el Nombre de quien desea modificar su RUC: ")
    if modificar in dic_clientes.keys():
        ruc_nuevo = int(input("Ingrese el nuevo RUC: "))
        dic_clientes[modificar] = ruc_nuevo
        print(modificar, "-", dic_clientes[modificar],
        "\nModificación con éxito.")
        print(dic_clientes) #solo lo puse para ver los cambios, lo borran
    else:
        print("Nombre no encontrado, no se puede cambiar.")


modificar_clientes()

l
#def acumular_puntos():

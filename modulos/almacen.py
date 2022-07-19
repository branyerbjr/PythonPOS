Lista_Productos = ["", "arror"]
Codigo_Product = ["#1234567", "#7654321"]
Stocks = [5, 10]
Precios = [12, 8]


def Selector_Productos():
    compras = []
    while True:
        compra = []
        k = 0
        print("\n+----+--------------------+---------+--------+----------+"
              "\n| N° | Nonbre de Producto |  Cod.   |  CANT. |  S/P.U.  |"
              "\n+----+--------------------+---------+--------+----------+")
        n = 0
        for i in Lista_Productos:
            k += 1
            print("| {:<2} | {:<18} | {:>8}| {:>4}   | {:>8.2f} |".format(
                k, i, Codigo_Product[n], Stocks[n], Precios[n]))
            print("+----+--------------------+---------+--------+----------+")
            n += 1
        select = int(input(f"Seleccione Cliente [1-{k}]: "))
        compra.append(Lista_Productos[select - 1])
        compra.append(Codigo_Product[select - 1])
        while True:
            cant = int(input("Ingrese la cantidad: "))
            if cant <= Stocks[select - 1]:
                compra.append(cant)
                compra.append(Precios[select - 1])
                total = Precios[select - 1] * cant
                compra.append(total)
                update = Stocks[select - 1] - cant
                Stocks[select - 1] = update
                compras.append(compra)
                break
            else:
                print("No hay stock")
                continue
        if str(input("Dale enter para continuar"
                     "\nTerminar de Registrar(s/n): ")) == 's':
            break
        else:
            continue
    return compras


def ini_Productos():
    while True:
        k = 0
        print("\n+----+--------------------+---------+--------+----------+"
              "\n| N° | Nonbre de Producto |  Cod.   |  CANT. |  S/P.U.  |"
              "\n+----+--------------------+---------+--------+----------+")
        for i in Lista_Productos:
            k += 1
            n = 0
            print("| {:<2} | {:<18} | {:>8}| {:>4}   | {:>8.2f} |".format(
                k, i, Codigo_Product[n], Stocks[n], Precios[n]))
            print("+----+--------------------+---------+--------+----------+")
            n += 1
        option = int(input("¿Que desea realizar?\n"
                           "[1] Agregar Nuevo Producto\n"
                           "[2] Modificar / Eliminar Producto\n"
                           "[3] SALIR\n"
                           "--> : "))
        if option == 1:
            agregar_producto()
        elif option == 2:
            select = int(input(f"Seleccione Producto [1-{k}]: "))
            option_1 = int(input("\t[1]Modificar\n"
                                 "\t[2]Eliminar\n"
                                 "\t[3]SALIR\n"
                                 "--> : "))
            if option_1 == 1:
                modificar_producto(select)
                continue
            elif option_1 == 2:
                eliminar_producto(select)
                print("\t__Elemento Eliminado__")
                continue
            elif option_1 == 3:
                continue
        elif option == 3:
            break


def agregar_producto():
    while True:
        pruducto = str(input("Ingrese Nuevo Producto: "))
        Lista_Productos.append(pruducto)
        cod = str(input("Ingrese Codigo de Producto: "))
        Codigo_Product.append(cod)
        catides = int(input("Ingrese Cantidad de stock: "))
        Stocks.append(catides)
        p_u = int(input("Ingrese Precio por Unidad: "))
        Precios.append(p_u)
        if str(input("¿Regresar al menu(s/n)?: ")) == 's':
            break
        else:
            continue


def modificar_producto(m):
    while True:
        options = str(input("\t¿Que desea Modificar?\n"
                            "\t[1] Nombre Poducto\n"
                            "\t[2] Codigo de Producto\n"
                            "\t[3] STOCK de Producto\n"
                            "\t[4] Precio de Producto\n"))
        if options == '1':
            Lista_Productos[m - 1] = str(input("Actualizar Nombre de Producto: "))
        elif options == '2':
            Codigo_Product[m - 1] = str(input("Actualizar Codigo: "))
        elif options == '3':
            Stocks[m - 1] = int(input("Actualizar Stock: "))
        elif options == '4':
            Precios[m - 1] = int(input("Actualizar Precio"))
        print("\n+--------------------+---------+--------+----------+"
              "\n| Nonbre de Producto |  Cod.   |  CANT. |  S/P.U.  |"
              "\n+--------------------+---------+--------+----------+")
        print("| {:<18} | {:>8}| {:>4}   | {:>8.2f} |".format(
            Lista_Productos[m - 1], Codigo_Product[m - 1], Stocks[m - 1], Precios[m - 1]))
        print("+----+--------------------+---------+--------+----------+")
        if str(input("¿Desea regresar al menu anterior(s/n)?: ")) == 's':
            break
        else:
            continue


def eliminar_producto(d):
    Lista_Productos.pop(d-1)
    Codigo_Product.pop(d-1)
    Stocks.pop(d-1)
    Precios.pop(d-1)

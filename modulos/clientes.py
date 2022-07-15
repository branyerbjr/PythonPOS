dic_clientes = {76233122: ['Jose Rodrigues', '-----NO----'], 76233123: ['Jose Rodrigues', '12365478251']}


def init_cliente():
    while True:
        keys = []
        k = 0
        print("+----+------------------+----------+-------------+"
              "\n| N° |NOMBRES           |   DNI    |    RUC      |"
              "\n+----+------------------+----------+-------------+")
        for clave, valor in dic_clientes.items():
            k += 1
            keys.append(clave)
            client = valor
            print("| {:<2} |{:<18}| {:>8} | {:>11} |".format(
                k, client[0], clave, client[1]))
            print("+----+------------------+----------+-------------+")
        option = int(input("¿Que desea realizar?\n"
                           "[1] Agregar Nuevo Cliente\n"
                           "[2] Modificar / Eliminar Cliente\n"
                           "[3] SALIR\n"
                           "-->: "))
        if option == 1:
            agregar_cliente()
        elif option == 2:
            select = int(input(f"Seleccione Cliente [1-{k}]: "))
            key = keys[select - 1]
            option_1 = int(input("[1]Modificar\n"
                                 "[2]Eliminar\n"
                                 "[3]SALIR\n"
                                 "-->: "))
            if option_1 == 1:
                modificar_cliente(key)
            elif option_1 == 2:
                dic_clientes.pop(key, "Cliente ya fue eliminado")
            elif option_1 == 3:
                continue
        elif option == 3:
            break


def agregar_cliente():
    while True:
        dni = int(input("Ingrese su DNI: "))
        nombre = input("Ingrese su nombre: ")
        option_ruc = str(input("¿Tiene RUC?(s/n): "))
        if option_ruc == 's':
            ruc = int(input("Ingrese RUC: "))
            dic_clientes[dni] = [nombre, ruc]
        else:
            dic_clientes[dni] = [nombre, '-----NO----']
        if input("Desea seguir agregando Clientes (s/n): ") == 'n':
            break
        else:
            continue


def modificar_cliente(dni):
    nombre = str(input("Modificar Nombre: "))
    option_ruc = str(input("Tiene RUC (s/n): "))
    if option_ruc == 's':
        ruc = int(input("Ingrese RUC: "))
        dic_clientes[dni] = [nombre, ruc]
    else:
        dic_clientes[dni] = [nombre, '-----NO----']


init_cliente()
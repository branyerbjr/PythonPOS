import datetime


def boleta_venta():
    x = datetime.datetime.now()
    t = x.strftime("%H:%M:%S %p")
    nombre = "arroz chevere"
    cantidad_vendida = 2
    precio = 12.3
    importe = 12.3
    total = precio + importe
    print("FECHA: ", x.date(), "\nHORA: ", x.strftime(" %H:%M:%S %p"))
    print("+-------------------------------------------------------+")
    print(f"| FACCTURA DE:                                          |\n"
          f"| PROYECTOFINAL                                         |\n"
          f"| AREQUIPA, PE-ARE, 04001                               |\n"
          f"|-------------------------------------------------------|\n"
          f"| COBRAR A:                                             |\n"
          f"|                         NUMERO DE BOLETA:           X |\n"
          f"| CLIENTENOMBRE            FECHA DE BOLETA:  {x.date()} |\n"
          f"|                           HORA DE BOLETA: {t} |\n"
          f"|                           MONTO ADEUDADO:           X |\n"
          f"| AREQUIPA, PE, 04001                                   |\n"
          f"|                                                       |")
    print("| +------------------+----------+----------+----------+ |")
    print("| |PRODUCTO          |CANT.     |PRECIO    |IMPORTE   | |")
    print("| +------------------+----------+----------+----------+ |")
    for i in range(3):
        print("| |{:<18}|{:>8}  |{:>10.2f}|{:>10.2f}| |".format(
             nombre, cantidad_vendida, precio, importe))
        print("| +------------------+----------+----------+----------+ |")
    print("|                               |TOTAL:    |{:>10.2f}| |".format(total))
    print("|                               +----------+----------+ |\n"
          "|             GRACIAS POR SU PREFERENCIA                |"
          "\n+-------------------------------------------------------+")



boleta_venta()

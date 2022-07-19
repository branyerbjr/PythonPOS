import datetime


def boleta_venta(compras, usuarios):
    archivo = open('facturas.txt', 'at')
    if str(usuarios[2]).isdigit():
        ruc = usuarios[2]
        n_ruc = "RUC"
    else:
        ruc = usuarios[0]
        n_ruc = "DNI"
    x = datetime.datetime.now()
    formato = x.strftime('%d/%m/%y')
    t = x.strftime("%H:%M:%S:%p")
    archivo.write("+-------------------------------------------------------+\n"
                  "| FACCTURA DE:                                          |\n"
                  "| PROYECTOFINAL                                         |\n"
                  "| AREQUIPA, PE-ARE, 04001                               |\n"
                  "|-------------------------------------------------------|\n"
                  "| COBRAR A:                                             |")
    archivo.write("\n| {:<8}           FECHA DE BOLETA: {:<8}    |".format(usuarios[1], formato))
    archivo.write("\n|                           HORA DE BOLETA: {:<11} |".format(t))
    archivo.write("\n| AREQUIPA, PE, 04001                                   |"
                  "\n|                               N° {:<3}: {:<11}     |".format(n_ruc, ruc))
    archivo.write("\n| +------------------+----------+----------+----------+ |"
                  "\n| |     PRODUCTO     |   CANT.  |  PRECIO  | IMPORTE  | |"
                  "\n| +------------------+----------+----------+----------+ |")
    monto = []
    cont = 0
    for i in compras:
        archivo.write("\n| |{:<18}|{:>8}  |{:>10.2f}|{:>10.2f}| |".format(
            compras[cont][0], compras[cont][2], compras[cont][3], compras[cont][4]))
        archivo.write("\n| +------------------+----------+----------+----------+ |")
        monto.append(compras[cont][4])
        cont += 1
    subtotal = sum(monto)
    igv = subtotal * 0.18
    total = subtotal + igv
    archivo.write("\n|                               |Subtotal: |{:>10.2f}| |".format(subtotal))
    archivo.write("\n|                               |IGV 18%:  |{:>10.2f}| |".format(igv))
    archivo.write("\n|                               |TOTAL:    |{:>10.2f}| |".format(total))
    archivo.write("\n|                                +----------+---------+ |"
                  "\n|             GRACIAS POR SU PREFERENCIA                |"
                  "\n+-------------------------------------------------------+"
                  "\n")
    archivo.close()


def Ver_boletas():
    archivo = open('facturas.txt', 'rt')
    contenido = archivo.read()
    print(contenido)
    archivo.close()


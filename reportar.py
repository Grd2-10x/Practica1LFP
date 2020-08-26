import webbrowser


def reporte(union, cadena2):
    cadena = [0] * len(cadena2)
    contador = 0
    tam = len(cadena)
    cant2 = len(union)
    for palabra in cadena2:
        cadena[contador] = palabra.lower()
        contador += 1
    cant = cadena[1]
    contador = 0

    if tam == 2 and int(cant) <= cant2 and cadena[0] == "reportar":
        with open('reporte.html', 'w') as miarchivo:
            miarchivo.write('<!DOCTYPE html>' + "\n")
            miarchivo.write('<html lang="en">' + "\n")
            miarchivo.write('<head>' + "\n")
            miarchivo.write('   <meta charset="UTF-8">' + "\n")
            miarchivo.write('   <title>Document</title>' + "\n")
            miarchivo.write('   <style type="text/css">' + "\n")
            miarchivo.write('       body{background: url(fondo.jpg);background-size: 100%;}' + "\n")
            miarchivo.write('h4{width: 400px;height: 40px;line-height: 60px;text-align: center;background: yellow;}'
                            + "\n")
            miarchivo.write('h3{width: 400px;height: 40px;line-height: 60px;text-align: center;background: SkyBlue;}'
                            + "\n")
            miarchivo.write('   </style>' + "\n")
            miarchivo.write('</head>' + "\n")
            miarchivo.write('<body>' + "\n")
            miarchivo.write('<center>' + "\n")

            for archivo in union:
                if contador != int(cant):
                    miarchivo.write(
                        "   <h3>" + str(contador + 1) + ") " + "Nombre: " + archivo.get('nombre') + "</h3>" + "\n")
                    miarchivo.write("   <h4>" + "Edad: " + str(archivo.get('edad')) + "</h4>" + "\n")
                    miarchivo.write("   <h4>" + "Activo: " + str(archivo.get('activo')) + "</h4>" + "\n")
                    miarchivo.write("   <h4>" + "Promedio: " + str(archivo.get('promedio')) + "</h4>" + "\n")
                    contador += 1
            miarchivo.write('</center>' + "\n")
            miarchivo.write('</body>' + "\n")
            miarchivo.write('</html>')
            miarchivo.close()
            print("Reporte Creado")
            webbrowser.open("reporte.html")

    else:
        print("Comando Invalido")

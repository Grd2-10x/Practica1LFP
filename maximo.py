def maximo(archivos, cadena):
    mayor = [0]*len(archivos)
    contador = 0
    comando = cadena[1].lower()
    if comando == "edad":
        print("Maximo edad")
        for archivo in archivos:
            mayor[contador] = archivo.get('edad')
            contador += 1
        mayor = max(mayor, key=int)
        return mayor
    elif comando == "promedio":
        print("Maximo Promedio")
        for archivo in archivos:
            mayor[contador] = archivo.get('promedio')
            contador += 1
        mayor = max(mayor, key=int)
        return mayor
    else:
        return "Comando invalido"

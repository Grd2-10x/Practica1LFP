def sumas(archivos, cadena):
    total = 0
    comando = cadena[1].lower()
    if comando == "edad":
        print("Sumando edad")
        for archivo in archivos:
            total += archivo.get('edad')
        return total
    elif comando == "promedio":
        print("Sumando Promedio")
        for archivo in archivos:
            total += archivo.get('promedio')
        return total
    else:
        return "Comando invalido"

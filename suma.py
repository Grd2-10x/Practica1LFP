def sumas(archivos, cadena):
    total = 0
    if cadena[1] == "edad":
        print("Sumando edad")
        for archivo in archivos:
            total += archivo.get('edad')
        return total
    elif cadena[1] == "promedio":
        print("Sumando Promedio")
        for archivo in archivos:
            total += archivo.get('promedio')
        return total
    else:
        return "Comando invalido"

def minimo(archivos, cadena):
    mayor = [0] * len(archivos)
    contador = 0
    if cadena[1] == "edad":
        print("Minimo edad")
        for archivo in archivos:
            mayor[contador] = archivo.get('edad')
            contador += 1
        mayor = min(mayor, key=int)
        return mayor
    elif cadena[1] == "promedio":
        print("Minimo Promedio")
        for archivo in archivos:
            mayor[contador] = archivo.get('promedio')
            contador += 1
        mayor = min(mayor, key=int)
        return mayor
    else:
        return "Comando invalido"

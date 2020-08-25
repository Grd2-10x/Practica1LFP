import json


def cargar(archivo):
    print("Cargando archivos")
    archivo1 = []
    for i in archivo:
        if i != "cargar" and i != "":
            try:
                with open(i, 'r') as miarchivo:
                    data = json.load(miarchivo)

                    archivo1 = archivo1 + data
                    miarchivo.close()
            except(OSError, IOError):
                data = "Archivo -" + i + "- no encontrado"
            print(data)
    return archivo1

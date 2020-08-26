# Manual De Usuario "SimpleQL"

## **Descripcion**
Aplicacion de consola "key insensitive" que permite a travez de comandos especificos, el manejo de atributos para archivos json con estructura definida para los atributos:
  * nombre
  * edad
  * activo
  * promedio

### **Menu Principal**
Se mostraran los comandos disponibles de la aplicacion:
 * cargar
 * seleccionar
 * maximo
 * Minimo
 * suma
 * cuenta
 * reportar
 * salir

Luego la consola solicitara el comando deseado, el primer comando siempre debera ser la carga de archivos, ya que si no se encuentran archivos cargados, al intentar ejecutar un comando distinto al de "cargar", se mostrara la siguiente advertencia: "No hay archivos cargados" y regresara al menu de comandos. *EL nombramiento de los archivos json no son key insensitive*

### **Comando Cargar**
Carga uno o "N" archivos json, almacenando los registros en memoria, de los "N" archivos json solicitados. *Solo cargara los archivos dentro del directorio de la aplicacion*
 1. Ejemplo: cargar archivo1.json, archivo2.json, archivo3.json, ... , archivon.json

### **Comando Seleccionar**
Realiza consultas especificas o generales de los registros almacenados en memoria.

Las consultas generales se realizan por un * que mostrará todos los registros.

Las consultas especificas se realizan por medio de parametros y una condición de busqueda "donde" para los registros almacenados.
 1. Ejemplo: SELECCIONAR *
 2. Ejemplo: seleccionar nombre,edad,activo
 3. Ejemplo: SELECCIONAR nombre,edad donde activo = true

### **Comando Maximo**
Realiza una busqueda dentro de los registros almacenados en memoria, mostrando el registro con la mayor edad o el mayor promedio.
 1. Ejemplo: MAXIMO edad
 2. Ejemplo: maximo promedio
 
### **Comando Minimo**
Realiza una busqueda dentro de los registros almacenados en memoria, mostrando el registro con la menor edad o el menor promedio.
 1. Ejemplo: MiNiMo edad
 2. Ejemplo: MINIMO promedio
 
### **Comando Suma**
Especificando la edad o el promedio, realiza una suma de todos los registros almacenados en memoria.
  1. Ejemplo: Suma edad
  2. Ejemplo: suma promedio
 
### **Comando Cuenta**
Realiza un recuento de todos los registros almacenados en memoria, mostrando los registros y la cantidad de registros almacenadas actualmente.
  1. Ejemplo: CueNTA
 
### **Comando Reportar**
Genera una pagina html atractiva con el numero de registros indicado, siempre que la cantidad ingresada sea menor o igual a la cantidad de registros almacenados en memoria actualmente. *suponiendo tener 20 registros en memoria*
 1. Ejemplo: reportar 1
 2. Ejemplo: REPORtar 5
 3. Ejemplo: REPORTAR 20
 4. Ejemplo: Reportar 0
 
### **Comando Salir**
Permite terminar la ejecucion de la aplicacion.
 1. Ejemplo: salir

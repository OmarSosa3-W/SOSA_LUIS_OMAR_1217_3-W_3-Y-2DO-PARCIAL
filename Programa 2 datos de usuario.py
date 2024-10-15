print() #para dejar una linea en blanco al ejecutar
print("SOSA LUIS OMAR 1217 3-W: MI PRACTICA DE DICCIONARIOS #2") #nombre del creador del codigo
print() #para dejar una linea en blanco al ejecutar

def obtener_datos_usuario(): #inicio de la funcion
    usuario = {}
    usuario['nombre'] = input("¿Cuál es tu nombre? ") #pide ingresar el nombre
    print() #para dejar una linea en blanco al ejecutar
    usuario['edad'] = input("¿Cuántos años tienes? ") #pide ingresar la edad
    print() #para dejar una linea en blanco al ejecutar
    usuario['direccion'] = input("¿Dónde vives? ") #pide ingresar el lugar de vivienda
    print() #para dejar una linea en blanco al ejecutar
    usuario['telefono'] = input("¿Cuál es tu número de teléfono? ") #pide ingresar el numero de telefono
    print() #para dejar una linea en blanco al ejecutar
    return usuario

print() #para dejar una linea en blanco al ejecutar
def mostrar_informacion(usuario):
    print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")

usuario = obtener_datos_usuario() #compara las variables para la ejecución
mostrar_informacion(usuario) #el resultado sera segun la funión 
print() #para dejar una linea en blanco al ejecutar
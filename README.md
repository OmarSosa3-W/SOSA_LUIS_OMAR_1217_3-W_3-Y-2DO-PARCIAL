# SOSA_LUIS_OMAR_1217_3-W_3ra ACTIVIDAD_2DO-PARCIAL
3 Y 2DO parcial

PROGRAMA 1: DIVISAS

print() #se coloca para dejar un espacio
print("SOSA LUIS OMAR 1217 3-W: MI PRÁCTICA DE DICCIONARIOS\n") #nombre del creador del codigo
print() #se coloca para dejar un espacio
divisas = { 
    "euro": "€",
    "dollar": "$",      #definindo las variables de de los euros     
    "yen": "¥"
} 

divisa_usuario = input("Introduce una divisa (euro, dollar, yen): ") #pide al usuario que ingrese una divisa 

simbolo = divisas.get(divisa_usuario) #clave para obtener el valor 

if simbolo: #si el simbolo esxiste
    print(f"El símbolo de la divisa '{divisa_usuario}' es: {simbolo}\n") #imprime en pantalla el simbolo de la divisa 
else:
    print(f"La divisa '{divisa_usuario}'está en el diccionario.\n") #muestra en pantalla el resultado de las divisas 
print() #se coloca para dejar un espacio

![image](https://github.com/user-attachments/assets/f8a99fd3-60d1-4740-adb7-c22ca99c08ff)
![image](https://github.com/user-attachments/assets/bed6a2f0-e691-476b-ad99-91036ef9e3be)

PROGRAMA 2: 

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

![image](https://github.com/user-attachments/assets/1e62948d-edea-40d5-b717-b6e089a3009c)
![image](https://github.com/user-attachments/assets/8b5fcb5d-6ac7-4e8e-870a-162012e919ee)


PROGRAMA 3: PRECIO DE FRUTAS 

print() #se coloca para una linea en blanco 
print("SOSA LUIS OMAR 1217 3-W: MI PRACTICA DE DICCIONARIOS #3") #nombre del creado de codigo
print() #se coloca para una linea en blanco 
def obtener_precio_fruta():
    precios_frutas = {
        'papaya': 2.5,
        'platano': 1.8,
        'naranja': 3.0,     #definir las variables en el dccionario
        'sandia': 2.7,
        'fresa': 4.0
    }

    fruta = input("¿Qué fruta te gustaría comprar? ") #pide ingresar una fruta del diccionario
    print() #se coloca para una linea en blanco 
    if fruta in precios_frutas: #las condiciones
        kilos = float(input(f"¿Cuántos kilos de {fruta} quieres? ")) #pide ingresar la cantidad de fruta que desea
        print() #se coloca para una linea en blanco 
        total = precios_frutas[fruta] * kilos
        print(f"El precio por {kilos} kilos de {fruta} es: ${total:.2f}") #muestra en pantallla el resultado 
        print() #se coloca para una linea en blanco 
    else:
        print(f"Lo siento, no tenemos {fruta} en este momento.") #si la fruta no esta en el menu
print() #se coloca para una linea en blanco 

obtener_precio_fruta()
print() #se coloca para una linea en blanco 

![image](https://github.com/user-attachments/assets/0e41da8d-ea51-4391-9364-d412f5141e31)
![image](https://github.com/user-attachments/assets/6a3131a7-4268-4b35-b870-9bc574947d08)

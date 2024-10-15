# SOSA_LUIS_OMAR_1217_3-W_3-Y-2DO-PARCIAL
3 Y 2DO parcial

PROGRAMA 1: DIVISAS

print() #se colca para dejar un espacio al momento de ejecutar
print("SOSA LUIS OMAR 1217 3-W: MI PRACTICA DE DICCIONARIOS") #creador del programa 
print() #se colca para dejar un espacio al momento de ejecutar
divisas = { "euro" : "€","dollar" : "$", "yen" : "¥"} #definir las palabras clave 
print() #se colca para dejar un espacio al momento de ejecutar

divisa_usuario = input("Introcude una divisa (euro, dollar, yen): ").lower() #pide ingresar una divisa
simbolo = divisas.get(divisa_usuario) #compara el valor ingresado 
print() #se colca para dejar un espacio al momento de ejecutar
if simbolo:
    print(f"el simbolo de la divisa {divisa_usuario} es: {simbolo}") #que pasa si la condicion se cumple 
    print() #se colca para dejar un espacio al momento de ejecutar
else:
    print(f"la divisa {divisa_usuario} esta en el diccionario.") #cuando la condicion se cumple mostrara ese mensaje -
    print() #se colca para dejar un espacio al momento de ejecutar
    
![image](https://github.com/user-attachments/assets/35fd7181-60d0-4041-bd45-4a7cf8d26b87)
![image](https://github.com/user-attachments/assets/05d67a01-df8d-482d-8645-40bcb02b8348)


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
        'manzana': 2.5,
        'platano': 1.8,
        'naranja': 3.0,     #definir las variables en el dccionario
        'pera': 2.7,
        'uvas': 4.0
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

![image](https://github.com/user-attachments/assets/81fc5d55-3a5c-4fbf-ba89-248a4e8fdc23)
![image](https://github.com/user-attachments/assets/c3daa01e-ac59-423e-98ab-f6015e35e71f)


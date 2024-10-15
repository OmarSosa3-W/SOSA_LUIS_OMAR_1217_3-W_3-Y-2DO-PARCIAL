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
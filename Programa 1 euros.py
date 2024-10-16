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
print()
if simbolo: #si el simbolo esxiste
    print(f"El símbolo de la divisa '{divisa_usuario}' es: {simbolo}\n") #imprime en pantalla el simbolo de la divisa 
else:
    print(f"La divisa '{divisa_usuario}'está en el diccionario.\n") #muestra en pantalla el resultado de las divisas 
print() #se coloca para dejar un espacio

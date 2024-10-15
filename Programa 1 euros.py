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
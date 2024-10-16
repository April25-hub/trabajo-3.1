print("Arzaba Diaz April")
print("3W")
print("1173")
#esta linea es el diccionario que relaciona las divisas con sus símbolos
divisas = {
    'euro': '€',
    'dollar': '$',
    'yen': '¥'
}

#esta linea solicitara al usuario que ingrese una divisa
entrada = input("introduce una divisa (euro, dollar, yen): ").strip().lower()

#esta linea verificara si la divisa ingresada esta en el diccionario
if entrada in divisas:
    #esta linea mostrara el simbolo de la divisa
    print(f"el simbolo de {entrada.capitalize()} es: {divisas[entrada]}")
else:
    #esta linea dara el mensaje si la divisa no está en el diccionario
    print("la divisa no esta en el diccionario")

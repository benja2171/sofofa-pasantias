
cadena = str(input("ingresa unas palabra:")) # se ingresa una palabra

if cadena == ''.join(reversed(cadena)): 
    print("es palidroma")
else:
    print("no es palidroma")
"""
Con un condicional hacemos uso del .join; 
este tienen como función unir las frases ingresadas luego con un reversed comparar la cadena de manera inversa, 
si se nota que son iguales a la original nos va a mostrar en pantalla que es palíndroma sino nos imprimirá que no lo es.
"""
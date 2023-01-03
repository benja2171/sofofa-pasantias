#para ingresar palabras y editarlas
Frase = input("ingresa una palabra:")
Frase = Frase.replace(".", "")#sacar llos puntos  del texto
Frase = Frase.replace(",", "")#sacar las comas del texto
Frase = Frase.replace("_", "")#sacar los guion bajon del texto
Frase = Frase.replace("-", "")#sacar los guiones del texto
Frase = Frase.replace("@", "a")#sacar el @  del texto
Frase = Frase.replace("á", "a")#sacar las letras a con tilde y reemplazarlas con letras a sin tilde en el  texto
Frase = Frase.replace("é", "e")#sacar las letras e con tilde y reemplazarlas con letras e sin tilde en el  texto
Frase = Frase.replace("í", "i")#sacar las letras i con tilde y reemplazarlas con letras i sin tilde en el  texto
Frase = Frase.replace("ó", "o")#sacar las letras o con tilde y reemplazarlas con letras o sin tilde en el  texto
Frase = Frase.replace("ú", "u")#sacar las letras u con tilde y reemplazarlas con letras u sin tilde en el  texto
print(Frase)# imprime las frase sin puntuaciones
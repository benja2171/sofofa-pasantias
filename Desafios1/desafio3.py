import math # importa una libreria para trunquear los decimales

print("ingresa tu rut sin digito verificador") #el print muestra en la terminal "ingresa tu rut sin digito verificador"

num1 = int(input(":" ))#variables al que se le ingresa el rut
num2 = int(input(":" ))
num3 = int(input(":" ))
num4 = int(input(":" ))
num5 = int(input(":" ))
num6 = int(input(":" ))
num7 = int(input(":" ))
num8 = int(input(":" ))

multiplicacionSuma = num8*2 + num7*3 + num6*4 + num5*5 + num4*6 + num3*7 + num2*2 + num1*3 #acá la variable multiplica y suma los numeros del rut

MultiplicacionDivision = multiplicacionSuma/11 #aquí en la variable MultiplicacionDivisión se divide la variable MultiplicacionSuma por 11

MulDivMul = math.trunc(MultiplicacionDivision)*11 # en la variable MulDivMul, math.trunc trunquea los decimales de la MultiplicacionDivisión y despues se multiplica por 11 

MulSuma = multiplicacionSuma - MulDivMul # en la variable MulS uma la MultiplicacionSuma se resta por MulDivMUL

RestaMulSuma = 11-MulSuma # en la variable RestMulSuma se hace una resta de 11 al MulSuma

if RestaMulSuma == 11: # esto es que si RestaMulSuma es = a 11 entonces mostrara en la terminal 0
    RestaMulSuma = 0
    print("su digito verificador es:" + str(RestaMulSuma))
elif RestaMulSuma == 10: # esto es que si RestaMulSuma es = a 10 entonces mostrara en la terminal k
    RestaMulSuma = "k"
    print("su digito verificador es:" + str(RestaMulSuma) )
else: # si no imprimira en la terminal RestaMulSuma
    print ("su digito verificador es:" + str(RestaMulSuma))

def crearTxt():
    archivo.write(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) +  str(num6) + str(num7) + str(num8) +"-"+ str(RestaMulSuma))
    archivo.close()
archivo = open("Rut.txt","w")
crearTxt()

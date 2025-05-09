#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
#  Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
if num < 0:
    negativo = True
    num = abs(num) 
else:
    negativo = False

inverso = 0
while num != 0:
    digito = num % 10
    inverso = inverso * 10 + digito
    num = num // 10

if negativo:
    inverso = -inverso

print("Número invertido:", inverso)

# Esta hoja fue utilizada para probar los codigos a medida que se iban creando, para que se pudieran correr en la terminal de manera individual. 
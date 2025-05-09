#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea.
comienzo = 0
final = 100
print(comienzo)
for const in range (comienzo, final):
    comienzo += 1
    print(comienzo);


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
nro = input("Ingrese un numero entero: "); 
contador = 0;
for caracter in nro: 
    contador += 1; 
print (f"El numero contiene {contador} digitos"); 


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, 
# excluyendo esos dos valores.
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))
suma = 0
mayor = max(a, b);
menor = min(a, b);

for nro in range(menor+1, mayor):
    suma += nro;
print(f"La suma de los enteros entre {menor} y {mayor}, excluyéndolos, es: {suma}")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

nro = int(input("ingrese un numero entero para sumarlo (ingrese 0 para detenerse): ")); 
total = 0;
while nro != 0:
    total += nro;
    nro = int(input("ingrese otro numero entero: ")); 
if total != 0:
    print("El total acumulado es", total); 


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

nro = random.randint(0,9);

contador = 0; 

intento = int(input("Ingrese un numero entre 0 y 9: "));

while intento != nro:
    if intento > 9 or intento < 0:
        print("El numero ingresado es incorrecto, ingrese un nro entre 0 y 9");
        contador += 1;
        
    else:
        print("El numero ingresado es incorrecto");
        contador += 1; 

    intento = int(input("Intente de nuevo ")); 

contador += 1 

print(f"Adivinaste el número en {contador} intentos.")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

inicio = -1
fin = 100 
for const in range (fin, inicio, -2): 
    print(const); 

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y 
# un número entero positivo indicado por el usuario.

inicio = 0
fin = int(input("Ingrese un numero entero positivo"))
suma = 0

if fin <= 0: 
    print("El numero ingresado no es correcto")
    fin = int(input("Ingrese un numero entero positivo"))

for nro in range(inicio, fin+1):
    suma += nro;
print(f"La suma de los enteros entre {inicio} y {fin} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar
# cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
total = 100;

pares = 0;
impares = 0; 
negativos = 0;
positivos = 0;

for i in range (total):
    nro = int(input("Ingrese un numero entero: ")); 
    if nro % 2 == 0:
        pares += 1; 
    else:
        impares +=1; 
    if nro >=0:
        positivos +=1;
    else:
        negativos +=1;
print(f"Hay un total de {pares} numeros pares, y un total de {impares} numeros impares. Tambien hay {positivos} positivo/s y {negativos} negativo/s.")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 

total = 100;
acumulador = 0; 

for i in range (total):
    nro = int(input("Ingrese un numero entero: ")); 
    acumulador += nro 
media = acumulador / total; 

print("El promedio o media de estos valores es", media); 

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
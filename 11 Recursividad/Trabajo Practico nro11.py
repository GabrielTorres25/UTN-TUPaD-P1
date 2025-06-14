#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario

def fact(n):
    if n == 0 or n == 1:
        return 1;
    else: 
        return n * fact(n - 1);
         
num = int(input("Ingrese un numero mayor que 1: ")); 

if num < 1:
    print("Porfavor ingrese un numero mayor que uno: "); 
else: 
    print(f"factoriales del 1 al {num}: ");
    for i in range(1, num + 1):
        print(f"{i} = {fact(i)}");

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

def fibonacci(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return fibonacci(n-1) + fibonacci(n-2);
    
posicion = int(input("Introduce una posicion de la serie de Fibonacci: ")); 
print("Serie de Fibonacci hasta la posicion", posicion, ":");
for i in range(posicion + 1):
    print(fibonacci(i));

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1;
    else:
        return base * potencia(base, exponente - 1);

Base = int(input("Ingresa la base: "));
Exponente = int(input("Introduce el exponente: "));

resultado = potencia(Base, Exponente);
print(f"{Base} elevado a la {Exponente} es: {resultado}"); 

#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 
def decimal(x):
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    else:
        return decimal(x // 2) + str(x % 2)

usuario = int(input(f"Ingrese un valor: ")); 

if usuario < 0:
    print("El número debe ser positivo.")
else:
    binario = decimal(usuario)
    print(f"La representación binaria de {usuario} es: {binario}") 


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
     #Requisitos: 
     # La solución debe ser recursiva. 
     # No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  
    if palabra[0] != palabra[-1]:
        return False 
    
    return es_palindromo(palabra[1:-1])

palabra = input("Introduce una palabra (sin espacios ni tildes): ").lower() ## para comparar que sean iguales 
if es_palindromo(palabra):
    print(f'"{palabra}" es un palindromo.')
else:
    print(f'"{palabra}" no es un palindromo.')


##6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
     #Restricciones: 
     # No se puede convertir el número a string. 
     # Usá operaciones matemáticas (%, //) y recursión. 
     # Ejemplos: 
     # suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
     # suma_digitos(9)      → 9 
     # suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n): 
    if n < 10:
        return n 
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(333)) ## retorna nueve
print(suma_digitos(1234)) ##   ""    diez 



##7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 
def contar_bloques(n):
    if n == 1:          
        return 1
    else:
        return n + contar_bloques(n - 1)

# Ejemplos de prueba
print(contar_bloques(1))  
print(contar_bloques(2))  
print(contar_bloques(4))  

##8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 
      #Ejemplos: 
      # contar_digito(12233421, 2)   → 3   
      # contar_digito(5555, 5)       → 4   
      # contar_digito(123456, 7)     → 0  

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

# Ejemplos de prueba
print(f"el numero 2 aparece {contar_digito(12233421, 2)}veces")  
print(contar_digito(5555, 5))      
print(contar_digito(123456, 7))    

##8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 
      #Ejemplos: 
      # contar_digito(12233421, 2)   → 3   
      # contar_digito(5555, 5)       → 4   
      # contar_digito(123456, 7)     → 0  

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

# Ejemplos de prueba
print(f"el numero 2 aparece {contar_digito(12233421, 2)} veces")  
print(f"el numero 5 aparece {contar_digito(5555, 5)} veces")  
print(f"el numero 7 aparece {contar_digito(123456, 7)} veces")
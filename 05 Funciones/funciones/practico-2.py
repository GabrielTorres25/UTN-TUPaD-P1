# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla
# el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    return print("Hola Mundo!");

imprimir_hola_mundo(); 

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

nombre = input("Ingresa tu nombre "); 

def saludar_usuario(nombre):
    return print("Hola", nombre)


saludar_usuario(nombre); 

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
# que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia): 
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresa tu nombre: ");
apellido = input("Ingresa tu apellido: ");
edad = input("Ingresa tu edad: ");
casa = input("¿Donde vivis?:");

informacion_personal(nombre, apellido, edad, casa); 

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
  
def calcular_area_circulo(radio): 
    return 3.14 * (radio ** 2) 


def calcular_perimetro_circulo(radio):
    return 3.14 * (radio * 2) 

usuario = int(input("Porfavor, ingrese el radio de un circulo.")); 

print(calcular_area_circulo(usuario)); 

print(calcular_perimetro_circulo(usuario)); 

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos 
# como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos
# y mostrar el resultado usando esta función.

def segundos_a_horas(segundos): 
    return segundos // 3600

usuario = int(input("Ingrese una cantidad de segundos, le devolveremos su equivalente en horas: ")); 

print(f"El equivalente de {usuario} segundos, es igual a {segundos_a_horas(usuario)} hs."); 

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
# y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero): 
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
usuario = int(input("Ingrese un numero: "))

tabla_multiplicar(usuario); 

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    division = a / b
    multiplicacion = a * b
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta}")
    print(f"{a} / {b} = {division}")
    print(f"{a} * {b} = {multiplicacion}")

primer_nro = int(input("Ingresa un numero: "))
segundo_nro = int(input("Ingresa un numero: "))

operaciones_basicas(primer_nro, segundo_nro); 

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc 

kg = float(input("Porfavor ingrese su peso en kilogramos: "));
mts = float(input("Porfavor ingrese su altura en metros: "));

resultado = calcular_imc(kg, mts); 
print(f"Tu índice de masa corporal (IMC) es: {resultado:.2f}")


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
# y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius): 
    return (celsius * 9/5) + 32

celsius = float(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva
# el promedio de ellos.Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c): 
    suma = a + b + c; 
    promedio = suma / 3; 
    return promedio

nro_uno = float(input("Ingrese un numero: "));
nro_dos = float(input("Ingrese un numero: "));
nro_tres = float(input("Ingrese un numero: "));

print(calcular_promedio(nro_uno, nro_dos, nro_tres)); 
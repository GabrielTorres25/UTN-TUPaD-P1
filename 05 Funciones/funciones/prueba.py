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
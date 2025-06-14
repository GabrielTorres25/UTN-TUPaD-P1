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
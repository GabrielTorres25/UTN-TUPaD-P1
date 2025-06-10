import time

def insertion_sort(lista):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1

        # Movemos los elementos de lista[0..i-1] que sean mayores que valor_actual
        # una posicion adelante de su posicion actual. 
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1

        # Insertamos el valor en la posicion correcta.
        lista[j + 1] = valor_actual

    return lista

# Ejemplo en consola
numeros = [5, 2, 9, 1, 5, 6]

# Medir tiempo de ejecución
t_inicio = time.time()
ordenados = insertion_sort(numeros.copy())
t_fin = time.time()

print("Lista ordenada:", ordenados)
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.")
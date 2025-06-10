## BUSQUEDA 

#  Busqueda Lineal
# Busca un elemento recorriendo toda la lista.
import time
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Definir la lista de ejemplo
lista = [9, 2, 4, 3, 6, 8, 1, 14, 12, 20]

# Medir tiempo de ejecución
t_inicio = time.time()
elemento = busqueda_lineal(lista, 8)
t_fin = time.time()

# Mostrar resultados
print(f"El elemento requerido se encuentra en la posición {elemento} de la lista.")
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.")


##eficiencia: O(n). Uso: Listas no ordenadas.

##2. Busqueda Binaria
##Solo funciona con listas ordenadas. Divide la lista a la mitad repetidamente.


import time
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Definir la lista de ejemplo
lista = [0, 2, 3, 4, 6, 8, 10, 15, 19, 20]

# Medir tiempo de ejecución
t_inicio = time.time()
elementoDos = busqueda_binaria(lista, 15)
t_fin = time.time()

# Mostrar resultados
print(f"El elemento requerido se encuentra en la posición {elementoDos} de la lista.")
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.")

#Eficiencia: O(log n) Uso: Listas ordenadas.


### ORDENAMIENTO 


##2. (Insertion Sort) Ordenamiento por insercion

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
ordenados = insertion_sort(numeros)
t_fin = time.time()

print("Lista ordenada:", ordenados)
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.")
#Eficiencia: O(n²), pero eficiente en listas pequeñas o casi ordenadas.

######


### Ordenamiento por seleccion (selection sort)
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Suponemos que el minimo esta en la posicion i
        indice_minimo = i

        # Buscamos el menor elemento en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambiamos el elemento actual con el menor encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    return lista

# ejemplo en consola
numeros = [29, 10, 14, 37, 13]

# Medir tiempo de ejecución
t_inicio = time.time()
ordenados = selection_sort(numeros)
t_fin = time.time()

print("Lista ordenada:", ordenados)
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.")



###Ordenamiento por Burbuja (Bubble Sort)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # En cada pasada, los elementos más grandes se desplazan hacia el final.
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Se realiza un intercambio si están en el orden incorrecto.
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo en consola con medidor de tiempo
numeros = [64, 34, 25, 12, 22, 11, 90]

t_inicio = time.time()
ordenados = bubble_sort(numeros)
t_fin = time.time()

print("Lista ordenada (bubble_sort):", ordenados)
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.\n")

###Ordenamiento por Burbuja Mejorado

def bubble_sort_optimizado(lista):
    n = len(lista)
    i = 0
    intercambio = True  # Inicializamos como True para entrar al bucle

    while i < n and intercambio:
        intercambio = False  # Se reinicia en cada pasada

        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True  # Se detecta un intercambio

        i += 1  # Avanzamos al siguiente ciclo

    return lista

# Ejemplo en consola con medidor de tiempo
t_inicio = time.time()
ordenados_opt = bubble_sort_optimizado(numeros)
t_fin = time.time()

print("Lista ordenada (bubble_sort_optimizado):", ordenados_opt)
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.")

## Quick Sort (Ordenamiento rápido)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # Caso base: lista vacía o con un solo elemento ya está ordenada

    # Elegimos el pivote (puede ser el primer elemento, el último, o aleatorio)
    pivote = lista[0]

    # Partimos la lista en listas menores, iguales y mayores al pivote
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    # Aplicamos recursión y combinamos
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso en consola
numeros = [10, 7, 8, 9, 1, 5]

# Medir tiempo de ejecución
t_inicio = time.time()
ordenados = quick_sort(numeros)
t_fin = time.time()

print("Lista ordenada:", ordenados)
print(f"Tiempo de ejecución: {t_fin - t_inicio:.10f} segundos.")


##Eficiencia promedio: O(n log n). Peor caso: O(n²) (si el pivote es mal elegido)





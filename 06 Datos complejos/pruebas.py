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
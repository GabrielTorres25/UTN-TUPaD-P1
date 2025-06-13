# bucle for para pedir los dni
dnis = [];

for i in range(3):  # 3 integrantes. 
    valido = False; 
    while not valido:
        dni = input(f"Ingresa el DNI del integrante {i+1}: ");
        if not dni.isdigit():
            print("Por favor ingresa solo numeros.");
        elif len(dni) < 7 or len(dni) > 9:
            print("El DNI debe tener entre 7 y 9 digitos.");
        else:
            dnis.append(dni);
            valido = True;

# bucle for para recorrer los dni
for dni in dnis:
    suma = 0
    frecuencia = [0] * 10  ## creamos una lista vacia con 10, 0.
    for digito in dni:      ## para registrar la frecuencia. 
        frecuencia[int(digito)] += 1
        suma += int(digito)

    print("////////////////////////////")
    print(f"DNI: {dni}")
    print(f"Suma de los digitos: {suma}")
    print("Frecuencia de cada digito:")
    for i in range(10):
        print(f"{i}: el numero aparece {frecuencia[i]} veces")
        
# conjuntos de digitos unicos por DNI
conjuntos_digitos = [set(dni) for dni in dnis]

# mostramos conjuntos de digitos
def mostrar_digitos(conjuntos):
    print("////////////////////////////")
    print("Conjuntos de digitos unicos por DNI");
    for i, conjunto in enumerate(conjuntos, 1):
        print(f"DNI {i}: {sorted(conjunto)}"); # Mostrar ordenado
    print("////////////////////////////")
# funcion con operaciones entre conjuntos de digitos
def operaciones_conjuntos(conjuntos):
    c1, c2, c3 = conjuntos

    union = c1 | c2 | c3
    interseccion = c1 & c2 & c3
    diferencia_1_2 = c1 - c2
    diferencia_1_3 = c1 - c3
    diferencia_2_3 = c2 - c3
    diferencia_simetrica = c1 ^ c2 ^ c3
## resultados 
    print("////////////////////////////")
    print("Operaciones entre conjuntos de dígitos")
    print(f"Unión de todos: {sorted(union)}") #el sorted para que los digitos aparezcan ordenados de menor a mayor 
    print(f"Intersección de todos: {sorted(interseccion)}") #facilitando su comparacion en este caso. 
    print(f"Diferencia DNI 1 - DNI 2: {sorted(diferencia_1_2)}")
    print(f"Diferencia DNI 1 - DNI 3: {sorted(diferencia_1_3)}")
    print(f"Diferencia DNI 2 - DNI 3: {sorted(diferencia_2_3)}")
    print(f"Diferencia simétrica entre todos: {sorted(diferencia_simetrica)}")

# ejecutamos las funciones
mostrar_digitos(conjuntos_digitos)
operaciones_conjuntos(conjuntos_digitos)

## Gabi Valdez
# Función para verificar si un año es bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Ingreso de años de nacimiento
años = []

for i in range(3):
    valido = False
    while not valido:
        try:
            año = int(input(f"Ingrese el año de nacimiento del integrante {i+1}: "))
            if año < 1900 or año > 2025:
                print("Por favor ingrese un año válido entre 1900 y 2025.")
            else:
                años.append(año)
                valido = True
        except ValueError:
            print("Por favor ingrese un número válido.")
# Contar pares e impares
pares = sum(1 for a in años if a % 2 == 0)
impares = len(años) - pares
print("////////////////////////////")
print(f"Años pares: {pares} - Años impares: {impares}")

# Grupo Z
if all(a > 2000 for a in años):
    print("Grupo Z")

# Año especial (bisiesto)
if any(es_bisiesto(a) for a in años):
    print("Tenemos un año especial")

# Calcular edades
anios_actual = 2025
edades = [anios_actual - a for a in años]

# Producto cartesiano (año x edad)
print("Producto cartesiano (año x edad):")
for a in años:
    for e in edades:
        print((a, e))
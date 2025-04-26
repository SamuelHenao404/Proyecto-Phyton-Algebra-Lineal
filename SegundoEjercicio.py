import numpy as np

# El mensaje codificado como una lista larga
valores_c = [
    -27, 11, 2, -3, 12, -12, 25, 3, 9, -2, 23, -3, -11, -10, -9, 17, 17, 1,
    -7, -16, -20, -15, 49, 139, 70, 63, 80, 180, 25, 49, 79, 16, 39, 95, 93,
    150, 99, 57, 133, 21, 47, 130, 24, 123, 27, 193, 20, 69, 96, 184, 39, 83,
    51, 6, 51, 117, 89, 140, 127, 43, 149, 17, 9, 122, -18, 79, 2, -148, -16,
    -34, -82, -140, -8, -42, -32, -2, -18, -82, -44, -98, -80, -18, -122, 10,
    16, -98, 40, -56, 39, 83, 62, 53, 56, 124, 17, 39, 39, 14, 27, 77, 61, 94,
    75, 25, 77, 19, 43, 92, 22, 69
]


# Convertimos los valores de C (mensaje codificado) en una matriz de 5 filas y 22 columnas
C = np.array(valores_c).reshape(5, 22)

# Definimos la matriz A
A = np.array([
    [0, 0, 1, -1, 0],
    [0, 4, -1, 1, 2],
    [-2, 4, 1, 1, 2],
    [2, -4, 0, 0, -2],
    [0, 2, -1, 1, 2]
])
#Imprimir a la matriz de codificación A y la matriz codificada  C
print("Punto a:\n")
print("Matriz A (Matriz de codificación):")
print(A)
print("\nMatriz C (Mensaje codificado):")
# Mostrar la matriz C con los corchetes y valores bien alineados
for i in range(C.shape[0]):
    print(f"[{' '.join(f'{int(x):5d}' for x in C[i])}]")
# Calculamos la inversa de A
A_inv = np.linalg.inv(A)

# Multiplicamos A_inv por cada columna de C (C tiene ahora 5 columnas y 22 filas)
B = A_inv @ C # Transponemos C para multiplicar correctamente

# Redondeamos los valores de B
B_redondeada = np.rint(B).astype(int)

#Imprimir b (matriz que contiene el mensaje que se desea codificar).
print("Punto b:")
print("\nMatriz B (mensaje descifrado):")
print(B_redondeada)
#Función para convertir número a letra (alfabeto español con Ñ)
def numero_a_letra_esp(n):
    alfabeto = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    if 1 <= n <= 27:
        return alfabeto[n - 1]
    else:
        return ' '  # Espacio si el número no corresponde a una letra válida

# Convertir la matriz B en una lista de letras
mensaje = ''.join(numero_a_letra_esp(int(n)) for n in B_redondeada.flatten())

#Mostrar mensaje oculto
print("Mensaje oculto:")
print(mensaje)
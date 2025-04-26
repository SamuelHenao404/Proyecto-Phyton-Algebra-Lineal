import numpy as np

# Definir la matriz S con vectores como columnas (no filas)
S = np.array([
    [1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [1, -1, 0, 0, 1, 1],
    [-1, 0, -1, -1, 1, -1],
    [0, -1, -2, 0, 1, 0],
    [1, 0, 0, 1, -1, 1]
])

# Verificar si el determinante es distinto de cero
det_S = np.linalg.det(S)

print("Determinante:", det_S)


# Verificar si el determinante es diferente de 0
es_base = det_S != 0

# Mostrar resultados
print("(a) ¿S es base de R^6?")
print("Determinante de la matriz:", det_S)
print("¿Es base?", "Sí ✅" if es_base else "No ❌")
# Parte (b) Obtener coordenadas del vector respecto a la base
v = np.array([7, -3, 6, 1, 4, -5])
coordenadas = np.linalg.solve(S, v)

print("\n(b) Coordenadas del vector (7, -3, 6, 1, 4, -5) en la base S:\n")
print(coordenadas)
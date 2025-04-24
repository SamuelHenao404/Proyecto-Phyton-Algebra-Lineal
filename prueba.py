# Importar las bibliotecas numpy y math
import numpy as np
import math

# Definir los vectores
u = np.array([24, 1, 6])
v = np.array([19, 37, -1])
w = np.array([34, -46, 7])
z = np.array([13, -4, 28])

# (a): Calcular (u + z - v) · (z - 3w + v)
parte1_a = u + z - v
parte2_a = z - 3*w + v
resultado_a = np.dot(parte1_a, parte2_a)

# (b): Calcular ||z - w|| - ||w × u||
norma1_b = np.linalg.norm(z - w)
producto_cruz = np.cross(w, u)
norma2_b = np.linalg.norm(producto_cruz)
resultado_b = norma1_b - norma2_b

# (c): Calcular ||u||(v + z) + ||2z - 3w|| * z
norma_u = np.linalg.norm(u)
suma_vz = v + z
parte1_c = norma_u * suma_vz
norma_2z_3w = np.linalg.norm(2*z - 3*w)
parte2_c = norma_2z_3w * z
resultado_c = parte1_c + parte2_c

# (d): Encontrar p y h tales que v = p + h, con p paralelo a u y h ortogonal a u
# p es la proyección de v sobre u
proyeccion_v_sobre_u = (np.dot(v, u) / np.dot(u, u)) * u
p = proyeccion_v_sobre_u
h = v - p  # Componente ortogonal

# Imprimir los resultados
print("a) Resultado del producto punto:", resultado_a)
print("b) Resultado de las normas:", resultado_b)
print("c) Resultado del vector combinado:", resultado_c)
print("d) Vector p (paralelo a u):", p)
print("d) Vector h (ortogonal a u):", h)

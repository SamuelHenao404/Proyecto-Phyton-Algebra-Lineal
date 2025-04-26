import numpy as np

# Definición de las funciones proporcionadas
SUMA = lambda u, w: np.array([[u[0,0] + w[0,0] + 2, u[0,1] + w[0,1] + 2]])
PRODUCTO = lambda alpha, u: np.array([[alpha + alpha*u[0,0] - 1, alpha + alpha*u[0,1] - 1]])

# --- Parte (a): Verificar que el elemento neutro aditivo es (0,0) = (-2,-2) ---
print("Parte (a): Verificación del elemento neutro aditivo")
u = np.array([[-2, -2]])  # Elemento neutro propuesto: (-2,-2)
w = np.array([[5, 33]])   # Vector w = (5,33)
sol_a = SUMA(u, w)        # Calculamos (-2,-2) ⊕ (5,33)

print("(-2, -2) ⊕ (5, 33) =", sol_a)

if np.allclose(sol_a, w):
    print("✅ Por lo tanto, (-2, -2) es el elemento neutro aditivo en (V, ⊕).")
else:
    print("❌ No se cumple la propiedad de neutro aditivo.")

# --- Parte (b): Calcular 8 ⊙ [(-11,3) ⊕ (5,-7)] ---
print("\nParte (b): Cálculo de 8 ⊙ [(-11,3) ⊕ (5,-7)]")
# Paso 1: Calcular (-11,3) ⊕ (5,-7)
u = np.array([[-11, 3]])
w = np.array([[5, -7]])
suma_b = SUMA(u, w)  # Suma: (-11+5+2, 3+(-7)+2) = (-4,-2)
print("  Suma intermedia (-11,3) ⊕ (5,-7):", suma_b)
# Paso 2: Calcular 8 ⊙ suma_b
alpha = 8
sol_b = PRODUCTO(alpha, suma_b)  # Producto: (8 + 8*(-4) - 1, 8 + 8*(-2) - 1) = (-25,-9)
print("Solución b:", sol_b)
# --- Parte (c): Calcular 8 ⊙ (-11,3) ⊕ 8 ⊙ (5,-7) ---
print("\nParte (c): Cálculo de 8 ⊙ (-11,3) ⊕ 8 ⊙ (5,-7)")
# Paso 1: Calcular 8 ⊙ (-11,3)
u = np.array([[-11, 3]])
prod_c1 = PRODUCTO(alpha, u)  # Producto: (8 + 8*(-11) - 1, 8 + 8*3 - 1) = (-81,31)
print("  Producto intermedio 8 ⊙ (-11,3):", prod_c1)
# Paso 2: Calcular 8 ⊙ (5,-7)
w = np.array([[5, -7]])
prod_c2 = PRODUCTO(alpha, w)  # Producto: (8 + 8*5 - 1, 8 + 8*(-7) - 1) = (47,-49)
print("  Producto intermedio 8 ⊙ (5,-7):", prod_c2)
# Paso 3: Calcular la suma prod_c1 ⊕ prod_c2
sol_c = SUMA(prod_c1, prod_c2)  # Suma: (-81+47+2, 31+(-49)+2) = (-32,-16)
print("Solución c:", sol_c)
# --- Parte (d): ¿Es V un espacio vectorial? ---
print("\nParte (d): ¿Es V un espacio vectorial?")
# Para que V sea un espacio vectorial, deben cumplirse todos los axiomas.
# Verificamos la distributividad de la multiplicación por escalar sobre la suma:
# α ⊙ (u ⊕ w) = (α ⊙ u) ⊕ (α ⊙ w)
# Usamos vectores genéricos y un escalar arbitrario
u = np.array([[1, 2]])
w = np.array([[3, 4]])
alpha = 5

# Lado izquierdo: α ⊙ (u ⊕ w)
suma_d = SUMA(u, w)
left = PRODUCTO(alpha, suma_d)
print("  Lado izquierdo α ⊙ (u ⊕ w):", left)

# Lado derecho: (α ⊙ u) ⊕ (α ⊙ w)
prod_d1 = PRODUCTO(alpha, u)
prod_d2 = PRODUCTO(alpha, w)
right = SUMA(prod_d1, prod_d2)
print("  Lado derecho (α ⊙ u) ⊕ (α ⊙ w):", right)

# Comparamos
if np.array_equal(left, right):
    print("  Distributividad se cumple (en este caso). Seguir verificando otros axiomas.")
else:
    print("  Distributividad no se cumple. V no es un espacio vectorial.")
    print("Solución d: No, V no es un espacio vectorial.")
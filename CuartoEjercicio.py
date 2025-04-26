import sympy as sp

# Parte (a)
p1 = (1, -3)
p2 = (-1, 5)
p3 = (-7, -4)

M = sp.Matrix([
    [p1[0], p1[1], 1],
    [p2[0], p2[1], 1],
    [p3[0], p3[1], 1]
])

area = sp.Rational(1,2) * abs(M.det())
print("(a) Área del triángulo ABC con puntos fijos:")
print("Área =", area)
# Declarar símbolo
k = sp.Symbol('k')

# Construir la matriz del triángulo
M = sp.Matrix([
    [k, -2, 1],
    [k, 1, 1],
    [-1, k, 1]
])

# Determinante
det = M.det()

# Área² = (1/4) * (det)**2, pero con fracción exacta
area_squared = sp.Rational(1, 4) * det**2

# Ecuación: área² = 81
eq = sp.Eq(area_squared, 81)

# Resolver la ecuación
soluciones = sp.solve(eq, k)

# Mostrar resultados
print("(b) Valores de k para los que el área² = 81 cm⁴:")
print(soluciones)
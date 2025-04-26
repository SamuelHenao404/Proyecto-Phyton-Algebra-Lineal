import sympy as sp

# Definimos la variable simbólica k
k = sp.Symbol('k')

# Definimos la matriz A
A = sp.Matrix([
    [-k,     k-1,   k+1,  k,    0],
    [ 1,      2,    -2,  -1,    1],
    [4-k,     k,   k+3, -k,     1],
    [-2,      3,     4,   6,    2],
    [ 0,      2,     1,   0,    4]
])

# Parte (a): valores de k donde A tiene inversa (det ≠ 0)

# Calcular det(A)
det_A = A.det()
print("Determinante de A:")
sp.pprint(det_A)

# Resolvemos det(A) ≠ 0
valores_k_inversible = sp.solve(sp.Eq(det_A, 0), k)

#Imprimimos valores en pantalla
print("\n(a) La matriz A tiene inversa para todo k excepto:")
for valor in valores_k_inversible:
    print(valor.evalf())
    # Parte (b): valores de k donde det(A) = 5 - 3k
sol_b = sp.solve(sp.Eq(det_A, 5 - 3*k), k)
# Mostrar los resultados numéricos
print("\n(b) Valores de k para los cuales det(A) = 5 - 3k:")
for valor in sol_b:
    print(valor.evalf())
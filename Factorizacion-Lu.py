from fractions import Fraction

def format_matrix(matrix):
    """Convierte los elementos de la matriz a texto en formato de fracción o número legible."""
    return [[str(val) for val in row] for row in matrix]

def print_matrix(name, matrix):
    """Imprime la matriz formateada y alineada."""
    print(f"\nMatriz {name}:")
    formatted = format_matrix(matrix)
    
    # Determinar el ancho máximo para alinear columnas
    col_widths = [max(len(item) for item in col) for col in zip(*formatted)]
    
    for row in formatted:
        print("[", end=" ")
        for i, val in enumerate(row):
            print(f"{val:>{col_widths[i]}}", end=" ")
        print("]")

print("==============================================")
print("     DESCOMPOSICIÓN LU PASO A PASO")
print("==============================================")

# 1. Ingresar el tamaño de la matriz
n = int(input("\nIngrese el tamaño de la matriz cuadrada (ej. 3 para 3x3): "))
print(f"\nSe creará una matriz de {n}x{n}.")

# 2. Ingresar los valores de la matriz
print("\n--- INGRESO DE LA MATRIZ A ---")
A = []
for i in range(n):
    fila = []
    print(f"\nFila {i+1}:")
    for j in range(n):
        # Permite ingresar fracciones (ej. 5/3) o enteros (ej. 2)
        val_str = input(f"  Elemento A[{i+1}][{j+1}]: ")
        fila.append(Fraction(val_str))
    A.append(fila)

print("\n==============================================")
print_matrix("A (Inicial)", A)
print("==============================================")

# 3. Inicializar L (Matriz Identidad) y U (Copia de A)
L = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
U = [row[:] for row in A]

# 4. Proceso de Descomposición LU con pasos detallados
print("\n--- INICIANDO ELIMINACIÓN GAUSSIANA ---")
paso = 1

for i in range(n - 1): # i es el índice de la fila pivote
    for k in range(i + 1, n): # k es el índice de la fila a modificar
        
        # Si el pivote es cero, la descomposición LU simple falla
        if U[i][i] == 0:
            print(f"\n¡ERROR! El pivote U[{i+1}][{i+1}] es cero. Se requiere intercambio de filas (PA=LU), lo cual no está soportado en esta versión básica.")
            exit()
            
        print(f"\n--- PASO {paso}: Haciendo cero el elemento debajo del pivote U[{i+1}][{i+1}] en la fila {k+1} ---")
        
        # Calcular el multiplicador
        multiplicador = U[k][i] / U[i][i]
        
        # Guardar en L
        L[k][i] = multiplicador
        
        print(f"Operación: Fila {k+1} -> Fila {k+1} - ({multiplicador}) * Fila {i+1}")
        print(f"Multiplicador l_{k+1}{i+1} = {multiplicador}")
        
        # Actualizar la fila k en U
        for j in range(i, n):
            U[k][j] = U[k][j] - multiplicador * U[i][j]
            
        print_matrix(f"U (Actualizada tras Paso {paso})", U)
        paso += 1

print("\n==============================================")
print("        RESULTADO FINAL")
print("==============================================")
print_matrix("L (Triangular Inferior)", L)
print_matrix("U (Triangular Superior)", U)
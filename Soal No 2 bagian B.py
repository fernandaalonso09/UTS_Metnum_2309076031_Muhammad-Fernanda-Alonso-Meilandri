# Muhammad Fernanda

import numpy as np

# Definisikan matriks A dan vektor B
A = np.array([[4, -1, -1],
              [-1, 4, 0],
              [-1, 0, 4]])  # Matriks koefisien

B = np.array([2, 6, 6])  # Vektor konstanta

# Fungsi untuk menghitung determinan matriks secara rekursif (dengan ekspansi kofaktor)
def determinant(A):
    # Basis: Jika A adalah matriks 2x2
    if A.shape == (2, 2):
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    
    det = 0
    for col in range(A.shape[1]):
        submatrix = np.delete(np.delete(A, 0, axis=0), col, axis=1)
        cofactor = ((-1) ** col) * A[0, col] * determinant(submatrix)
        det += cofactor
    return det

# Fungsi untuk menghitung matriks kofaktor
def cofactor_matrix(A):
    n = A.shape[0]
    C = np.zeros_like(A)
    
    for i in range(n):
        for j in range(n):
            submatrix = np.delete(np.delete(A, i, axis=0), j, axis=1)
            C[i, j] = ((-1) ** (i + j)) * determinant(submatrix)
    
    return C

# Fungsi untuk menghitung invers matriks dengan metode ekspansi kofaktor
def inverse_matrix(A):
    det_A = determinant(A)
    if det_A == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinannya 0.")
    
    C = cofactor_matrix(A)  # Matriks kofaktor
    adjugate = C.T  # Matriks adjoin adalah transpose dari kofaktor
    A_inv = adjugate / det_A  # Invers matriks
    
    return A_inv

# Menghitung invers matriks A menggunakan metode ekspansi kofaktor
A_inv = inverse_matrix(A)

# Menyelesaikan sistem linier x = A^-1 * B
x = np.dot(A_inv, B)

# Menampilkan hasil
print("Hasil penyelesaian x1, x2, dan x3 menggunakan metode ekspansi kofaktor adalah:")
print(f"x1 = {x[0]:.10f}")
print(f"x2 = {x[1]:.10f}")
print(f"x3 = {x[2]:.10f}")

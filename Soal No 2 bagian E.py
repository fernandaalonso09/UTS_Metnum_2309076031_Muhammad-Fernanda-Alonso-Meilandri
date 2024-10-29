import numpy as np

def cofactor_determinant(matrix):
    """
    Fungsi untuk menghitung determinan matriks menggunakan ekspansi kofaktor.
    Parameters:
    matrix (ndarray): Matriks persegi (n x n).
    Returns:
    float: Determinan dari matriks.
    """
    if matrix.shape[0] == 1:
        return matrix[0, 0]
    if matrix.shape[0] == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    
    det = 0
    for c in range(matrix.shape[1]):
        minor = np.delete(np.delete(matrix, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * matrix[0, c] * cofactor_determinant(minor)
    
    return det

def adjoint(matrix):
    """
    Fungsi untuk menghitung adjoin dari matriks persegi.
    Parameters:
    matrix (ndarray): Matriks persegi (n x n).
    Returns:
    ndarray: Matriks adjoin (n x n).
    """
    adj = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            adj[j, i] = ((-1) ** (i + j)) * cofactor_determinant(minor)
    return adj

def inverse_matrix(matrix):
    """
    Fungsi untuk menghitung inverse dari matriks persegi menggunakan metode adjoin.
    Parameters:
    matrix (ndarray): Matriks persegi (n x n).
    Returns:
    ndarray: Matriks invers (n x n) jika determinan tidak nol.
    """
    det = cofactor_determinant(matrix)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinan nol.")
    
    adj = adjoint(matrix)
    return adj / det

# Definisikan matriks koefisien A untuk memastikan bahwa A dikenali
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)

# Menghitung invers dari matriks koefisien
try:
    inverse_A = inverse_matrix(A)
    print("Inverse dari matriks koefisien:\n", inverse_A)
except ValueError as e:
    print(e)
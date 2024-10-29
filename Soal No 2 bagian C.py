import numpy as np

# Definisi matriks A dan B seperti yang digunakan dalam bagian A dan B
A = np.array([[4, -1, -1],
              [-1, 4, 0],
              [-1, 0, 4]])  # Matriks koefisien

B = np.array([2, 6, 6])  # Vektor konstanta

# Fungsi dari metode Jacobi yang digunakan di bagian A
def jacobi(A, B, x0, max_iterations, tolerance):
    n = len(B)
    x = np.copy(x0)
    
    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)
        
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (B[i] - s) / A[i, i]
        
        # Periksa konvergensi
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new
        
        x = x_new
    
    return x

# Fungsi dari metode ekspansi kofaktor yang digunakan di bagian B
def determinant(A):
    if A.shape == (2, 2):
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    
    det = 0
    for col in range(A.shape[1]):
        submatrix = np.delete(np.delete(A, 0, axis=0), col, axis=1)
        cofactor = ((-1) ** col) * A[0, col] * determinant(submatrix)
        det += cofactor
    return det

def cofactor_matrix(A):
    n = A.shape[0]
    C = np.zeros_like(A)
    
    for i in range(n):
        for j in range(n):
            submatrix = np.delete(np.delete(A, i, axis=0), j, axis=1)
            C[i, j] = ((-1) ** (i + j)) * determinant(submatrix)
    
    return C

def inverse_matrix(A):
    det_A = determinant(A)
    if det_A == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinannya 0.")
    
    C = cofactor_matrix(A)  # Matriks kofaktor
    adjugate = C.T  # Matriks adjoin adalah transpose dari kofaktor
    A_inv = adjugate / det_A  # Invers matriks
    
    return A_inv

# Fungsi Gauss-Seidel dengan struktur yang mirip dengan Jacobi (memanfaatkan hasil Jacobi dan ekspansi kofaktor)
def gauss_seidel(A, B, x0, max_iterations, tolerance):
    n = len(B)
    x = np.copy(x0)
    
    for iteration in range(max_iterations):
        x_old = np.copy(x)
        
        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))
            sum2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (B[i] - sum1 - sum2) / A[i, i]
        
        # Periksa konvergensi dengan cara yang mirip Jacobi
        error = np.linalg.norm(x - x_old, ord=np.inf)
        
        if error < tolerance:
            print(f"Konvergen setelah {iteration+1} iterasi.")
            break
    
    return x

# Nilai awal x0 dan parameter untuk iterasi
x0 = np.zeros_like(B)  # Inisialisasi dengan nilai nol
max_iterations = 100  # Maksimal 100 iterasi
tolerance = 1e-10  # Toleransi error

# Jalankan metode Gauss-Seidel dengan memanfaatkan metode sebelumnya
x_solution = gauss_seidel(A, B, x0, max_iterations, tolerance)

# Tampilkan hasil
print("Solusi untuk x1, x2, dan x3 menggunakan metode Gauss-Seidel adalah:")
print(f"x1 = {x_solution[0]:.10f}")
print(f"x2 = {x_solution[1]:.10f}")
print(f"x3 = {x_solution[2]:.10f}")

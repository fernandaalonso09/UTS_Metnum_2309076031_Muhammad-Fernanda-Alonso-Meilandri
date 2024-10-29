import numpy as np

# Definisikan matriks A (koefisien) dan vektor B (konstanta)
A = np.array([[4, -1, -1],
              [-1, 4, 0],
              [-1, 0, 4]])  # Matriks koefisien

B = np.array([2, 6, 6])  # Vektor konstanta

# Fungsi untuk metode eliminasi Gauss-Jordan
def gauss_jordan(A, B):
    n = len(B)
    # Membentuk matriks augmented [A | B]
    augmented_matrix = np.hstack([A, B.reshape(-1, 1)])
    
    # Eliminasi Gauss-Jordan
    for i in range(n):
        # Pivoting: Membuat elemen diagonal utama menjadi 1
        pivot = augmented_matrix[i, i]
        augmented_matrix[i] = augmented_matrix[i] / pivot
        
        # Eliminasi elemen di atas dan di bawah diagonal
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]
    
    # Solusi adalah kolom terakhir dari augmented_matrix
    x = augmented_matrix[:, -1]
    
    return x

# Jalankan metode Gauss-Jordan
x_solution = gauss_jordan(A, B)

# Tampilkan hasil
print("Solusi untuk x1, x2, dan x3 menggunakan metode eliminasi Gauss-Jordan adalah:")
print(f"x1 = {x_solution[0]:.10f}")
print(f"x2 = {x_solution[1]:.10f}")
print(f"x3 = {x_solution[2]:.10f}")

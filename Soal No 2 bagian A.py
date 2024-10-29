import numpy as np

# Definisikan matriks A (koefisien) dan vektor B (konstanta)
A = np.array([[4, -1, -1],
              [-1, 4, 0],
              [-1, 0, 4]])  # Matriks koefisien

B = np.array([2, 6, 6])  # Vektor konstanta

# Menggunakan metode eliminasi Gauss untuk menyelesaikan sistem Ax = B
# np.linalg.solve merupakan metode langsung untuk menyelesaikan sistem persamaan linier
x = np.linalg.solve(A, B)

# Menampilkan hasil
print("Hasil penyelesaian untuk x1, x2, dan x3 adalah:")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])

# Muhammad Fernanda Alonso Meilandri 
# 2309076031
# 
import numpy as np
import matplotlib.pyplot as plt

# Definisikan parameter-parameter yang digunakan
L = 0.5  # Induktansi dalam Henry (H)
C = 10e-6  # Kapasitansi dalam Farad (F)

# Fungsi untuk menghitung frekuensi resonansi berdasarkan nilai R
def f_R(R):
    """
    Menghitung frekuensi resonansi f(R) untuk nilai resistansi R.
    Akan mengembalikan None jika tidak ada solusi riil (nilai negatif dalam akar).
    """
    term = (1/(L*C)) - (R**2)/(4*L**2)
    if term < 0:
        return None  # Tidak ada solusi riil
    return (1/(2 * np.pi)) * np.sqrt(term)

# Rentang nilai resistansi yang akan dihitung
R_values = np.linspace(0, 100, 1000)  # Nilai resistansi dari 0 hingga 100 ohm
f_values = [f_R(R) for R in R_values]  # Menghitung frekuensi untuk setiap nilai R

# Hapus nilai None (di mana tidak ada solusi riil)
R_values_filtered = [R for R, f in zip(R_values, f_values) if f is not None]
f_values_filtered = [f for f in f_values if f is not None]

# Plot hasil
plt.plot(R_values_filtered, f_values_filtered)
plt.xlabel('Resistansi (R) [Ohm]')
plt.ylabel('Frekuensi (f) [Hz]')
plt.title('Plot Frekuensi vs Resistansi')
plt.grid(True)
plt.show()

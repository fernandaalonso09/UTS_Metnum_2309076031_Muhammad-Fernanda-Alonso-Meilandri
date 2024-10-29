import numpy as np

# Fungsi untuk menghitung nilai R berdasarkan temperatur T
def R(T):
    return 5000 * np.exp(3500 * (1/T - 1/298))

# Fungsi untuk menghitung nilai eksak dari turunan dR/dT
def exact_derivative(T):
    return R(T) * (-3500 / T**2)

# Fungsi turunan menggunakan metode selisih maju
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Fungsi turunan menggunakan metode selisih mundur
def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

# Fungsi turunan menggunakan metode selisih tengah
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Rentang temperatur dan nilai h
temperatures = np.arange(250, 351, 10)  # Dari 250K sampai 350K dengan interval 10K
h = 0.01  # Nilai h kecil untuk pendekatan numerik

# Inisialisasi daftar untuk menyimpan galat relatif
forward_errors = []
backward_errors = []
central_errors = []

# Hitung galat relatif pada setiap temperatur
for T in temperatures:
    # Hitung nilai eksak dan nilai pendekatan
    exact_val = exact_derivative(T)
    forward_val = forward_difference(R, T, h)
    backward_val = backward_difference(R, T, h)
    central_val = central_difference(R, T, h)
    
    # Hitung galat relatif untuk setiap metode
    forward_error = abs((exact_val - forward_val) / exact_val)
    backward_error = abs((exact_val - backward_val) / exact_val)
    central_error = abs((exact_val - central_val) / exact_val)
    
    # Simpan galat relatif
    forward_errors.append(forward_error)
    backward_errors.append(backward_error)
    central_errors.append(central_error)

# Tampilkan hasil dalam bentuk tabel
print(f"{'T (K)':<8} {'Forward Error':<15} {'Backward Error':<15} {'Central Error':<15}")
print("="*50)
for i, T in enumerate(temperatures):
    print(f"{T:<8} {forward_errors[i]:<15.6f} {backward_errors[i]:<15.6f} {central_errors[i]:<15.6f}")

"""1. Fungsi R(T), exact_derivative(T), forward_difference, backward_difference, dan central_difference:
Fungsi ini sama dengan yang digunakan sebelumnya untuk menghitung nilai , turunan eksak, serta turunan menggunakan metode numerik.
2. Galat Relatif:
forward_error, backward_error, dan central_error dihitung menggunakan rumus galat relatif untuk setiap metode pada setiap temperatur.
3. Menampilkan Hasil:
Hasil galat relatif untuk setiap metode pada setiap temperatur ditampilkan dalam bentuk tabel."""
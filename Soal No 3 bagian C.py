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

# Inisialisasi daftar untuk menyimpan hasil
forward_results = []
backward_results = []
central_results = []
exact_results = []

# Hitung turunan pada setiap temperatur
for T in temperatures:
    forward_results.append(forward_difference(R, T, h))
    backward_results.append(backward_difference(R, T, h))
    central_results.append(central_difference(R, T, h))
    exact_results.append(exact_derivative(T))

# Tampilkan hasil dalam bentuk tabel
print(f"{'T (K)':<8} {'Forward':<15} {'Backward':<15} {'Central':<15} {'Exact':<15}")
print("="*60)
for i, T in enumerate(temperatures):
    print(f"{T:<8} {forward_results[i]:<15.6f} {backward_results[i]:<15.6f} {central_results[i]:<15.6f} {exact_results[i]:<15.6f}")

"""Sedikit penjelasan:
R(T): Menghitung resistansi  untuk temperatur .
exact_derivative(T): Menghitung nilai eksak dari turunan .
forward_difference, backward_difference, central_difference: Masing-masing menghitung turunan dengan metode selisih maju, mundur, dan tengah.
2. Pengaturan Rentang Temperatur dan Nilai h:
temperatures: Array dari 250K hingga 350K dengan interval 10K.
h = 0.01: Jarak kecil untuk pendekatan numerik.
3. Perhitungan dan Penyimpanan Hasil:
Loop menghitung turunan di setiap temperatur menggunakan metode selisih maju, mundur, tengah, serta nilai eksak, dan menyimpannya dalam daftar masing-masing.
4. Menampilkan Hasil:
Menampilkan hasil dalam bentuk tabel dengan kolom T (K), Forward, Backward, Central, dan Exact."""
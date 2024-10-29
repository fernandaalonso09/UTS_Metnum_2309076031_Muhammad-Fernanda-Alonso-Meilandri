import numpy as np

# Fungsi untuk menghitung nilai R berdasarkan temperatur T
def R(T):
    """
    Fungsi untuk menghitung resistansi R sebagai fungsi dari temperatur T.
    Parameters:
    T (float): Temperatur dalam Kelvin.
    Returns:
    float: Nilai resistansi R dalam Ohm.
    """
    return 5000 * np.exp(3500 * (1/T - 1/298))

# Fungsi untuk menghitung turunan menggunakan metode selisih maju
def forward_difference(f, x, h):
    """
    Menghitung turunan menggunakan metode selisih maju.
    Parameters:
    f (function): Fungsi yang akan diturunkan.
    x (float): Titik di mana turunan dihitung.
    h (float): Jarak antara titik.
    Returns:
    float: Estimasi turunan di titik x.
    """
    return (f(x + h) - f(x)) / h

# Fungsi untuk menghitung turunan menggunakan metode selisih mundur
def backward_difference(f, x, h):
    """
    Menghitung turunan menggunakan metode selisih mundur.
    Parameters:
    f (function): Fungsi yang akan diturunkan.
    x (float): Titik di mana turunan dihitung.
    h (float): Jarak antara titik.
    Returns:
    float: Estimasi turunan di titik x.
    """
    return (f(x) - f(x - h)) / h

# Fungsi untuk menghitung turunan menggunakan metode selisih tengah
def central_difference(f, x, h):
    """
    Menghitung turunan menggunakan metode selisih tengah.
    Parameters:
    f (function): Fungsi yang akan diturunkan.
    x (float): Titik di mana turunan dihitung.
    h (float): Jarak antara titik.
    Returns:
    float: Estimasi turunan di titik x.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

# Parameter untuk pengujian
T_test = 300  # Temperatur di mana turunan akan dihitung (misalnya 300 K)
h = 0.01      # Nilai h kecil untuk pendekatan numerik

# Hitung turunan menggunakan masing-masing metode
forward_result = forward_difference(R, T_test, h)
backward_result = backward_difference(R, T_test, h)
central_result = central_difference(R, T_test, h)

# Tampilkan hasil
print(f"Turunan menggunakan metode selisih maju pada T={T_test}K: {forward_result}")
print(f"Turunan menggunakan metode selisih mundur pada T={T_test}K: {backward_result}")
print(f"Turunan menggunakan metode selisih tengah pada T={T_test}K: {central_result}")
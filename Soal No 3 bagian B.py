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

# Fungsi untuk menghitung nilai eksak dari turunan dR/dT
def exact_derivative(T):
    """
    Fungsi untuk menghitung turunan eksak dari R(T) terhadap T.
    Parameters:
    T (float): Temperatur dalam Kelvin.
    Returns:
    float: Nilai eksak turunan dR/dT pada T.
    """
    return R(T) * (-3500 / T**2)

# Parameter untuk pengujian
T_test = 300  # Temperatur di mana turunan eksak akan dihitung (misalnya 300 K)

# Hitung nilai eksak turunan
exact_result = exact_derivative(T_test)

# Tampilkan hasil
print(f"Nilai eksak turunan dR/dT pada T={T_test}K: {exact_result}")

"""Penjelasan

1. Fungsi R(T): Menghitung nilai resistansi  berdasarkan temperatur .


2. Fungsi exact_derivative(T): Menghitung nilai eksak dari turunan  berdasarkan persamaan yang diberikan.


3. Parameter Pengujian:

T_test adalah temperatur yang digunakan untuk menghitung turunan, di sini diasumsikan 300 K.



4. Output"""
# Muhammad Fernanda Alonso Meilandri
# 2309076031
# Teknik Elktro
import numpy as np
import matplotlib.pyplot as plt

def R(T):
    """
    Menghitung resistansi R sebagai fungsi dari suhu T dalam Kelvin.
    
    Parameter:
    T (float): Suhu dalam Kelvin.
    
    Mengembalikan:
    float: Resistansi R dalam ohm.
    """
    return 5000 * np.exp(3500 * ((1 / T) - (1 / 298)))

def turunan_selisih_maju(fungsi, T, h):
    """
    Menghitung turunan numerik menggunakan metode selisih maju.
    
    Parameter:
    fungsi (callable): Fungsi yang akan dihitung turunannya.
    T (float): Titik di mana turunan dievaluasi.
    h (float): Ukuran langkah.
    
    Mengembalikan:
    float: Turunan numerik pada T.
    """
    return (fungsi(T + h) - fungsi(T)) / h

def turunan_selisih_mundur(fungsi, T, h):
    """
    Menghitung turunan numerik menggunakan metode selisih mundur.
    
    Parameter:
    fungsi (callable): Fungsi yang akan dihitung turunannya.
    T (float): Titik di mana turunan dievaluasi.
    h (float): Ukuran langkah.
    
    Mengembalikan:
    float: Turunan numerik pada T.
    """
    return (fungsi(T) - fungsi(T - h)) / h

def turunan_selisih_tengah(fungsi, T, h):
    """
    Menghitung turunan numerik menggunakan metode selisih tengah.
    
    Parameter:
    fungsi (callable): Fungsi yang akan dihitung turunannya.
    T (float): Titik di mana turunan dievaluasi.
    h (float): Ukuran langkah.
    
    Mengembalikan:
    float: Turunan numerik pada T.
    """
    return (fungsi(T + h) - fungsi(T - h)) / (2 * h)

def ekstrapolasi_richardson(fungsi, T, h, n=2):
    """
    Menerapkan Ekstrapolasi Richardson untuk meningkatkan akurasi turunan selisih tengah.
    
    Parameter:
    fungsi (callable): Fungsi yang akan dihitung turunannya.
    T (float): Titik di mana turunan dievaluasi.
    h (float): Ukuran langkah awal.
    n (int): Orde Ekstrapolasi Richardson (default adalah 2).
    
    Mengembalikan:
    float: Perkiraan turunan yang lebih akurat pada T.
    """
    # Tabel Richardson
    tabel = np.zeros((n, n))
    
    # Mengisi kolom pertama dengan turunan selisih tengah pada ukuran langkah yang berkurang
    for i in range(n):
        tabel[i, 0] = turunan_selisih_tengah(fungsi, T, h / (2 ** i))
    
    # Menerapkan rumus Ekstrapolasi Richardson
    for j in range(1, n):
        for i in range(n - j):
            tabel[i, j] = (4*j * tabel[i + 1, j - 1] - tabel[i, j - 1]) / (4*j - 1)
    
    return tabel[0, n - 1]

# Rentang suhu dan ukuran langkah
suhu = np.arange(250, 351, 10)
h = 1e-2  # Ukuran langkah kecil untuk perhitungan turunan awal

# Menghitung turunan dengan masing-masing metode
turunan_maju = [turunan_selisih_maju(R, T, h) for T in suhu]
turunan_mundur = [turunan_selisih_mundur(R, T, h) for T in suhu]
turunan_tengah = [turunan_selisih_tengah(R, T, h) for T in suhu]
turunan_richardson = [ekstrapolasi_richardson(R, T, h) for T in suhu]

# Plot hasil perbandingan
plt.plot(suhu, turunan_maju, label="Selisih Maju", marker="o")
plt.plot(suhu, turunan_mundur, label="Selisih Mundur", marker="s")
plt.plot(suhu, turunan_tengah, label="Selisih Tengah", marker="^")
plt.plot(suhu, turunan_richardson, label="Ekstrapolasi Richardson", marker="d")
plt.xlabel("Suhu (K)")
plt.ylabel("dR/dT (ohm/K)")
plt.title("Perbandingan Metode untuk Menghitung Turunan dR/dT")
plt.legend()
plt.grid(True)
plt.show()

"""1. turunan_selisih_maju: Menghitung turunan dengan selisih maju.
2. turunan_selisih_mundur: Menghitung turunan dengan selisih mundur.
3. turunan_selisih_tengah: Menghitung turunan dengan selisih tengah.
4. ekstrapolasi_richardson: Menghitung turunan dengan Ekstrapolasi Richardson untuk akurasi lebih tinggi.
Grafik akan menunjukkan perbandingan hasil turunan  dari setiap metode. Hasil ini membantu 
memahami metode mana yang lebih akurat (biasanya Ekstrapolasi Richardson memberikan
 hasil paling akurat) dan bagaimana masing-masing metode mendekati nilai turunan sebenarnya"""
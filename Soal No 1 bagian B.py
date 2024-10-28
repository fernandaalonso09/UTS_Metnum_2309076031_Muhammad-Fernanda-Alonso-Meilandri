# Muhammad Fernanda Alonso Meilandri
# 2309076031
# Teknik Elektro
#
import numpy as np

# Didefinisikan nilai-nilai L, C (soal dengan yang disoal), dan target frekuensi
L = 0.5  # Induktansi dalam Henry (H)
C = 10e-6  # Kapasitansi dalam Farad (F)
target_f = 1000  # Frekuensi resonansi target dalam Hz

def f_R(R):
    """
    Menghitung frekuensi resonansi f(R) untuk nilai R yang diberikan.
    
    Parameters:
    R (float): Resistansi dalam ohm.
    
    Returns:
    float: Frekuensi resonansi dalam Hertz.
    """
    try:
        term = (1/(L*C)) - (R**2)/(4*L**2)
        if term < 0:
            raise ValueError("Nilai di dalam akar negatif, tidak ada solusi riil.")
        return (1/(2 * np.pi)) * np.sqrt(term)
    except ValueError as e:
        return None

def bisection_method(func, target, a, b, tol):
    """
    Mencari akar dari fungsi menggunakan metode bisection.
    
    Parameters:
    func (callable): Fungsi yang akan dicari akarnya.
    target (float): Nilai target yang diinginkan (seperti f(R) = 1000 Hz).
    a (float): Batas bawah interval.
    b (float): Batas atas interval.
    tol (float): Toleransi error.
    
    Returns:
    float: Nilai R yang menghasilkan frekuensi sesuai target dalam toleransi yang diberikan.
    """
    if func(a) is None or func(b) is None:
        raise ValueError("Salah satu nilai di batas interval tidak memiliki solusi riil.")
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        f_mid = func(midpoint) - target
        
        if f_mid == 0 or (b - a) / 2.0 < tol:
            return midpoint
        elif (func(a) - target) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

# Implementasi metode bisection untuk mencari R yang menghasilkan f(R) = 1000 Hz
a = 0  # Batas bawah interval
b = 100  # Batas atas interval
tol = 0.1  # Toleransi error dalam ohm

try:
    R_solution = bisection_method(f_R, target_f, a, b, tol)
    print(f"Nilai R yang menghasilkan frekuensi 1000 Hz adalah: {R_solution:.4f} ohm")
except ValueError as e:
    print(f"Error: {e}")

# Muhammad Fernanda Alonso Meilandri
# 2309076031
# Teknik Elektro
#UTS
import numpy as np

# Didefinisikan ulang nilai-nilai L, C, dan target frekuensi
L = 0.5  # Induktansi dalam Henry (H)
C = 10e-6  # Kapasitansi dalam Farad (F)
target_f = 1000  # Frekuensi resonansi target dalam Hz

def f_R(R):
    """
    Menghitung frekuensi resonansi f(R) untuk nilai R yang diberikan.
    
    Parameters:
    R (float): Resistansi dalam ohm.
    
    Returns:
    float: Frekuensi resonansi dalam Hertz, atau None jika tidak ada solusi riil.
    """
    try:
        term = (1/(L*C)) - (R**2)/(4*L**2)
        if term < 0:
            return None  # Tidak ada solusi riil
        return (1/(2 * np.pi)) * np.sqrt(term)
    except ValueError as e:
        return None

def df_dR(R):
    """
    Menghitung turunan f'(R) terhadap R.
    
    Parameters:
    R (float): Resistansi dalam ohm.
    
    Returns:
    float: Turunan f'(R) terhadap R, atau None jika tidak ada solusi riil.
    """
    try:
        term = (1/(L*C)) - (R**2)/(4*L**2)
        if term <= 0:
            return None  # Tidak ada solusi riil untuk turunan
        numerator = -R / (2 * L**2)
        denominator = np.sqrt(term)
        return (1/(2 * np.pi)) * (numerator / denominator)
    except ValueError as e:
        return None

def newton_raphson(func, dfunc, target, x0, tol, max_iter):
    """
    Mencari akar dari fungsi menggunakan metode Newton-Raphson.
    
    Parameters:
    func (callable): Fungsi yang akan dicari akarnya.
    dfunc (callable): Turunan dari fungsi tersebut.
    target (float): Nilai target yang diinginkan (seperti f(R) = 1000 Hz).
    x0 (float): Tebakan awal.
    tol (float): Toleransi error.
    max_iter (int): Jumlah iterasi maksimal.
    
    Returns:
    float: Nilai R yang menghasilkan frekuensi sesuai target dalam toleransi yang diberikan.
    """
    x = x0
    for i in range(max_iter):
        f_val = func(x)
        if f_val is None:
            raise ValueError(f"Tidak ada solusi riil untuk nilai R = {x}")
        
        f_val = f_val - target
        df_val = dfunc(x)
        
        if df_val is None or df_val == 0:
            raise ValueError(f"Turunan nol atau tidak valid untuk R = {x}, metode Newton-Raphson gagal.")
        
        x_new = x - f_val / df_val
        
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
        
    raise ValueError("Metode tidak konvergen setelah iterasi maksimal.")

# Implementasi metode Newton-Raphson untuk mencari R yang menghasilkan f(R) = 1000 Hz
R0 = 50  # Tebakan awal untuk R
tol = 0.1  # Toleransi error
max_iter = 100  # Iterasi maksimal

try:
    R_solution = newton_raphson(f_R, df_dR, target_f, R0, tol, max_iter)
    print(f"Nilai R yang menghasilkan frekuensi 1000 Hz adalah: {R_solution:.4f} ohm")
except ValueError as e:
    print(f"Error: {e}")


# Tidak ada solusi riil dikarenakan tebakan awal yang terlalu jauh 
# sehingga menyebabkan hasil berbeda dengan metode biscetion

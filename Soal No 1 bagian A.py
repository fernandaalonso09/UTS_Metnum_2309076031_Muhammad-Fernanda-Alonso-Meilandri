#Muhammad Fernanda Alonso Meilandri
#2309076031
#Teknik Elektro
import numpy as np

# Didefinisikan nilai-nilai L dan C Sesuai dengan Soal yang diberikan
L = 0.5  # Induktansi dalam Henry (H)
C = 10e-6  # Kapasitansi dalam Farad (F)

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
        print(f"Error: {e}")
        return None

def df_dR(R):
    """
    Menghitung turunan f'(R) terhadap R.
    
    Parameters:
    R (float): Resistansi dalam ohm.
    
    Returns:
    float: Turunan f'(R) terhadap R.
    """
    try:
        term = (1/(L*C)) - (R**2)/(4*L**2)
        if term <= 0:
            raise ValueError("Nilai di dalam akar negatif atau nol.")
        numerator = -R / (2 * L**2)
        denominator = np.sqrt(term)
        return (1/(2 * np.pi)) * (numerator / denominator)
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Contoh pengujian dengan nilai R yang berbeda
R_values = [10, 20, 30, 40, 50]
for R in R_values:
    frekuensi = f_R(R)
    turunan_frekuensi = df_dR(R)
    print(f"R = {R} ohm -> f(R) = {frekuensi:.4f} Hz, f'(R) = {turunan_frekuensi:.4f} Hz/ohm")

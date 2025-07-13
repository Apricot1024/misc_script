import math
import numpy as np
from scipy.interpolate import CubicSpline

def read_dedx_data(filepath):
    energies = []
    dedx = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('!') or not line.strip():
                continue
            parts = line.split()
            # 第三列为能量，第四列为阻止本领
            try:
                energy = float(parts[2]) * 1.008
                dedx_val = float(parts[3])
                energies.append(energy)
                dedx.append(dedx_val)
            except (IndexError, ValueError):
                continue
    return np.array(energies), np.array(dedx)

def dedx_spline(energy, filepath="../data/dEdxpinO.txt"):
    energies, dedx = read_dedx_data(filepath)
    cs = CubicSpline(energies, dedx)
    return cs(energy)

v_light = 3e8  # Speed of light in m/s
h = 4.135e-15  # Planck's constant in eV·s
e = 1.602e-19  # Elementary charge in C

m_i = 931.5e6  # Mass of the incident particle in eV/c²
z = 1  # Charge state of the Incident particle
# tke = 64.5e3  # TKE of the Incident particle in eV
tke = 70e3
# tke = 193e3  # TKE of the Incident particle in eV
M = 52 * 2 + 17 * 3  # Mass number of the target nucleus
m = 1  # Mass number of the incident particle
m_t = 17 # Mass number of the target nucleus
m_1 = 52 # Mass number of the other nucleus in target (Cr)
m_2 = 16 # Mass number of the other nucleus in target (O)
wg = 10e-9  # Resonance strength in eV
# wg = 1.66e-3  # Resonance strength in eV
detector_efficiency = 0.069  # Detector efficiency
# e_eff = 99e-15 # Effective stopping cross section in ev atoms^-1 cm^2

# e_dedx = 0.375792  # Energy loss in MeV mg^-1 cm^2
# e_dedx = 0.356704
e_dedx_O = dedx_spline(tke / 1e6, "./data/dEdxpinO.txt")  # Energy loss in MeV mg^-1 cm^2
e_dedx_Cr = dedx_spline(tke / 1e6, "./data/dEdxpinCr.txt")  # Energy loss in MeV mg^-1 cm^2
# e_dedx = 3 / 2.1 * e_dedx_O + 2 / 2.1 * e_dedx_Cr  # Total energy loss in MeV mg^-1 cm^2
e_dedx = 2.1 / 2.1 * e_dedx_O * m_t + 2 / 2.1 * e_dedx_Cr * m_1 + 0.7 / 2.1 * e_dedx_O * m_2
e_eff = (
    (2.1 / 2.1 * e_dedx_O * m_t + 2 / 2.1 * e_dedx_Cr * m_1 + 0.7 / 2.1 * e_dedx_O * m_2) * 1e6 / 1e-3 * 1.66e-24 * m_t / (m_t + m)
    # e_dedx * 1e6 / 1e-3 * 1.66e-24 * M * M / (M + m)
)  # Effective stopping cross section in eV atoms^-1 cm^2
# e_eff = 91.6e-15  # Effective stopping cross section in ev atoms^-1 cm^2

print(f"e_dedx: {e_dedx}")
print(f"e_dedx_O: {e_dedx_O}, e_dedx_Cr: {e_dedx_Cr}, e_eff: {e_eff}")
p = math.sqrt(2 * m_i * tke)  # Momentum of the Incident particle in eV/c

lambda_in = h / p * v_light * 100  # de Broglie wavelength in cm

print(lambda_in)

n_out = (
    lambda_in**2 * wg * detector_efficiency / (2 * e_eff * z * e)
)  # yield in atoms/C

print(n_out)

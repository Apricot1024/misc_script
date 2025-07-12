import math

v_light = 3e8  # Speed of light in m/s
h = 4.135e-15  # Planck's constant in eV·s
e = 1.602e-19  # Elementary charge in C

m_i = 931.5e6  # Mass of the incident particle in eV/c²
z = 1  # Charge state of the Incident particle
# tke = 64.5e3  # TKE of the Incident particle in eV
tke = 193e3  # TKE of the Incident particle in eV
M = 52 * 2 + 17 * 3  # Mass number of the target nucleus
m = 1  # Mass number of the incident particle
# wg = 10e-9  # Resonance strength in eV
wg = 1.66e-3  # Resonance strength in eV
detector_efficiency = 0.069  # Detector efficiency
# e_eff = 99e-15 # Effective stopping cross section in ev atoms^-1 cm^2

# e_dedx = 0.375792  # Energy loss in MeV mg^-1 cm^2
e_dedx = 0.356704
e_eff = (
    e_dedx * 1e6 / 1e-3 * 1.66e-24 * M * M / (M + m)
)  # Effective stopping cross section in eV atoms^-1 cm^2
# e_eff = 91.6e-15  # Effective stopping cross section in ev atoms^-1 cm^2

print(e_eff)

p = math.sqrt(2 * m_i * tke)  # Momentum of the Incident particle in eV/c

lambda_in = h / p * v_light * 100  # de Broglie wavelength in cm

print(lambda_in)

n_out = (
    lambda_in**2 * wg * detector_efficiency / (2 * e_eff * z * e)
)  # yield in atoms/C

print(n_out)

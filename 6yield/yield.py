import math

v_light = 3e8 # Speed of light in m/s
h = 4.135e-15 # Planck's constant in eV·s
e = 1.602e-19 # Elementary charge in C
m = 931.5e6 # Mass of a proton in eV/c²
# tke = 64.5e3 # TKE of the proton in eV
tke = 193e3 # TKE of the proton in eV
z = 1 # Charge state of the proton

# wg = 10e-9 # Resonance strength in eV
wg = 1.66e-6 # Resonance strength in eV
detector_efficiency = 0.1 # Detector efficiency
# e_eff = 99e-15 # Effective stopping cross section in ev atoms^-1 cm^2
e_eff = 91.6e-15 # Effective stopping cross section in ev atoms^-1 cm^2

p = math.sqrt(2 * m * tke)  # Momentum of the proton in eV/c 

lambda_in = h / p * v_light * 100  # de Broglie wavelength in cm

print(lambda_in)

n_out = lambda_in**2 * wg * detector_efficiency / (2 * e_eff * z * e)

print(n_out)

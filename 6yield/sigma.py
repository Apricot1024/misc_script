import math
import matplotlib.pyplot as plt

v_light = 3e8  # Speed of light in m/s
h = 4.135e-15  # Planck's constant in eV·s
e = 1.602e-19  # Elementary charge in C
PI = math.pi  # Pi constant

m_i = 931.5e6  # Mass of the incident particle in eV/c²
z1 = 1  # Charge state of the Incident particle
z2 = 8  # Charge state of the target nucleus
M = 52 * 2 + 17 * 3  # Mass number of the target nucleus
m1 = 1  # Mass number of the incident particle

m2 = 17  # Mass number of the target nucleus
ER = 64.5e3  # TKE of the resonance in eV in Center of Mass frame
G_a = 130.0  # Total Width of the resonance in eV
wg = 10e-9  # Resonance strength in eV

# ER = 183.3e3  # TKE of the resonance in eV in Center of Mass frame
# G_a = 6.8  # Total Width of the resonance in eV
# wg = 1.66e-3  # Resonance strength in eV


p = math.sqrt(2 * m_i * ER)  # Momentum of the Incident particle in eV/c
lambda_in = h / p * v_light * 100  # de Broglie wavelength in cm

# 计算能区范围
E_min = ER - 15 * G_a
E_max = ER + 15 * G_a
# E_min = ER - 80 * G_a
# E_max = ER + 80 * G_a

# 计算sigma
results = []
for E in range(int(E_min), int(E_max) + 1):
    sigma = (PI * lambda_in**2 * wg * G_a) / ((E - ER) ** 2 + (G_a / 2) ** 2) * 1e24
    E = E * 1e-6  # 转换为MeV
    SF = (
        E
        * sigma
        * (math.exp(0.98951013 * z1 * z2 * math.sqrt((m1 * m2) / (m1 + m2) / E)))
    )
    E = E * 18 / 17 # 转换为实验室系能量
    results.append((E, sigma, SF))

# 输出结果
with open("data/sigma_result.txt", "w") as f:
    f.write("E\tsigma\tSF\n")
    for E, sigma, SF in results:
        f.write(f"{E}\t{sigma}\t{SF}\n")

with open(f"data/sfactor_{ER}.txt", "w") as f:
    f.write("E\tSF\n")
    for E, sigma, SF in results:
        f.write(f"{E}\t{SF}\n")

# 画图
E_list = [E for E, _, _ in results]
sigma_list = [sigma for _, sigma, _ in results]
SF_list = [SF for _, _, SF in results]
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(E_list, sigma_list, label=r"$\sigma(E)$")
plt.xlabel("E (keV)")
plt.ylabel(r"$\sigma$ [b]")
plt.title("Resonance Cross Section")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(E_list, SF_list, label="SF", color="orange")
plt.xlabel("E (keV)")
plt.ylabel("S-factor [MeV-b]")
plt.title("SF vs Energy")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("fig/sigma_plot.png")
plt.show()

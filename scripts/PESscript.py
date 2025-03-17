import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load Excel file
file_name = "HYQCalculations.xlsx"
sheet_name = "HYQ PES Python"

df = pd.read_excel(file_name, sheet_name=sheet_name)

# Ensure "States" is used as the index
df.set_index("States", inplace=True)

# Extract relevant states and their energies
states = ["S1", "S2", "S5", "T1", "T2", "T5"]  
energies = df.loc[states, "Energy (eV)"].values

# Convert to relative energies using S0 as reference
S0_energy = df.loc["S0", "Energy (eV)"]
relative_energies = energies - S0_energy

# 1D PES
plt.figure(figsize=(6, 5))
plt.scatter(states, relative_energies, color='red', s=100, label="Excited States")
plt.plot(states, relative_energies, linestyle='--', color='black', alpha=0.5)

# Labels
plt.xlabel("Electronic States")
plt.ylabel("Relative Energy (eV)")
plt.title("1D Potential Energy Surface of HYQ")
plt.ylim(min(relative_energies) - 0.5, max(relative_energies) + 1)
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("PES_1D.png", dpi=300)
plt.show()

# 2D PES
reaction_coord = np.linspace(0, len(states) - 1, len(states))

plt.figure(figsize=(6, 5))
plt.plot(reaction_coord, relative_energies, marker='o', linestyle='-', color='red')

# Labels
plt.xlabel("Reaction Coordinate (Arbitrary Units)")
plt.ylabel("Relative Energy (eV)")
plt.title("2D PES of HYQ Along Reaction Coordinate")
plt.xticks(reaction_coord, states)
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("PES_2D.png", dpi=300)
plt.show()

# 3D PES
x = np.array([0, 1, 2, 3, 4, 5])  # First reaction coordinate
y = np.array([0, 1, 2, 3, 4, 5])  # Second reaction coordinate
X, Y = np.meshgrid(x, y)

# Energy values for the 3D surface plot
Z = np.array([relative_energies for _ in range(len(x))])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')

# Labels
ax.set_xlabel("Reaction Coordinate 1")
ax.set_ylabel("Reaction Coordinate 2")
ax.set_zlabel("Relative Energy (eV)")
ax.set_title("3D PES of HYQ")
plt.savefig("PES_3D.png", dpi=300)
plt.show()
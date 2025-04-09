import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

methods = ['B3LYP', 'B3LYP', 'PBE0', 'PBE0', 'PBE', 'PBE']
frequencies = [3891.49, 3892.86, 3823.65, 3824.88, 3711.45, 3712.79]
epsilon = [0.016748, 0.01323, 0.014514, 0.010553, 0.011792, 0.008784]
intensities = [84.64, 66.86, 73.35, 53.33, 59.59, 44.39]

# Map methods to numerical values for X-axis
method_map = {'B3LYP': 0, 'PBE0': 1, 'PBE': 2}
x = [method_map[m] for m in methods]
y = frequencies
z = intensities

# Create 3D scatter plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(x, y, z, c=z, cmap='plasma', s=100)

# Label axes
ax.set_xlabel('Method')
ax.set_ylabel('Frequency (cm⁻¹)')
ax.set_zlabel('IR Intensity (km/mol)')
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['B3LYP', 'PBE0', 'PBE'])

# Add colorbar
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Intensity (km/mol)')

plt.tight_layout()
plt.show()

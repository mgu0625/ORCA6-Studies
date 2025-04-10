import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ['B3LYP', 'PBE0', 'PBE']
frequencies = {
    'B3LYP': [3891.49, 3892.86],
    'PBE0': [3823.65, 3824.88],
    'PBE':  [3711.45, 3712.79]
}
intensities = {
    'B3LYP': [84.64, 66.86],
    'PBE0': [73.35, 53.33],
    'PBE':  [59.59, 44.39]
}

# Setting up figure with 3 stacked subplots (shared x-axis)
fig, axes = plt.subplots(3, 1, figsize=(8, 6), sharex=True)

# Plot styling
colors = {'B3LYP': '#c7b0ec', 'PBE0': '#ecc7b0', 'PBE': '#b0ecc7'}
peak_width = 1.2

# Loop through methods and plot in separate subplots
for ax, method in zip(axes, methods[::-1]):  # reverse order 
    for freq, inten in zip(frequencies[method], intensities[method]):
        x = np.linspace(freq - 20, freq + 20, 200)
        y = -np.exp(-((x - freq)**2) / (2 * peak_width**2)) * inten / 100
        ax.plot(x, y, color=colors[method])
        ax.text(freq, min(y)-0.05, f'{inten:.1f} km/mol', fontsize=8, ha='center', va='top')
    
    ax.set_ylabel(method, fontsize=10, rotation=0, labelpad=30)
    ax.set_yticks([])
    ax.set_xlim(3700, 3900)
    ax.set_facecolor('#f9f9f9')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)




# formatting
axes[-1].set_xlabel("Wavenumber (cm⁻¹)")
plt.suptitle("Simulated IR Spectra of O–H Stretching Modes", fontsize=12)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.gca().invert_xaxis()

plt.tight_layout()
plt.savefig("OH_freq_comparison_GS.png", dpi=300)  
plt.show()
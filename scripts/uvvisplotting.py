import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# load file
file_name = "HYQCalculations.xlsx"

# find the sheet with TDDFT data
xls = pd.ExcelFile(file_name)
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    if "wavelength (nm)" in df.columns and "fosc" in df.columns:
        print(f"Found TDDFT data in sheet: {sheet}")
        break
else:
    raise ValueError("No sheet with 'wavelength (nm)' and 'fosc' found!")

# extract λ and fosc
wavelengths = df["wavelength (nm)"].dropna().astype(float)
osc_strengths = df["fosc"].dropna().astype(float)

# define gaussian broadening function
def gaussian_broadening(x, x0, f, sigma):
    """Gaussian broadening for each excitation."""
    return f * np.exp(-((x - x0) ** 2) / (2 * sigma ** 2))

# generate smooth spec
x_smooth = np.linspace(min(wavelengths) - 10, max(wavelengths) + 10, 1000)
sigma = 10  

y_smooth = np.zeros_like(x_smooth)
for w, f in zip(wavelengths, osc_strengths):
    y_smooth += gaussian_broadening(x_smooth, w, f, sigma)

# plot smoothed uv-vis spec
plt.figure(figsize=(8, 6))
plt.plot(x_smooth, y_smooth, color="b", label="Gaussian Broadening")
plt.scatter(wavelengths, osc_strengths, color="r", marker="o", label="Raw TDDFT Peaks") 


# plot settup
plt.xlabel("Wavelength (nm)", fontsize=12)
plt.ylabel("Oscillator Strength (f)", fontsize=12)
plt.gca().invert_xaxis()  # Invert x-axis (standard for UV-Vis)
plt.grid(True, linestyle="--", alpha=0.6)

# save plot
plt.savefig("HYQ_TDDFT_UVVis.png", dpi=300, bbox_inches="tight")

plt.show()


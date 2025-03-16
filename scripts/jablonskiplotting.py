import pandas as pd
import matplotlib.pyplot as plt

# load file and locate tab
file_name = "HYQCalculations.xlsx"
sheet_name = "HYQ TDDFT Python"

# read the sheet
df = pd.read_excel(file_name, sheet_name=sheet_name)

# extract extract
state_labels = df["excited state labels"].astype(str)  # Ensure labels are strings
excitation_energies = df["excitation energy (eV)"].astype(float)  # Convert to float

# separating singlet and triplet states
singlet_states = df[df["excited state labels"].str.startswith("s")] 
triplet_states = df[df["excited state labels"].str.startswith("t")] 

# setting up the figure
fig, ax = plt.subplots(figsize=(5, 6))
ax.set_ylabel("Energy (eV)", fontsize=14)  # Label the y-axis
ax.set_ylim(0, max(excitation_energies) + 0.5)  # Adjust energy scale

# plot singlet states(L)
for label, energy in zip(singlet_states["excited state labels"], singlet_states["excitation energy (eV)"]):
    ax.hlines(y=energy, xmin=0.2, xmax=0.4, color="black", linewidth=1)  # Black line for singlets
    ax.text(0.5, energy, label, verticalalignment="center", fontsize=9, color="purple", fontweight="bold")

# plot triplet states(R)
for label, energy in zip(triplet_states["excited state labels"], triplet_states["excitation energy (eV)"]):
    ax.hlines(y=energy, xmin=0.6, xmax=0.8, color="red", linewidth=1)  # Red line for triplets
    ax.text(0.85, energy, label, verticalalignment="center", fontsize=9, color="purple", fontweight="bold")

# remove x-axis labels and ticks
ax.set_xticks([])
ax.set_xticklabels([])

plt.savefig("jablonski_diagram.png", dpi=300, bbox_inches="tight")
plt.show()


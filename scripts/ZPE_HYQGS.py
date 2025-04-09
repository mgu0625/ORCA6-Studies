import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

functionals = ['PBE0', 'B3LYP', 'PBE']
zpe_values = [68.98, 68.25, 2.51]
colors = ['#ecc7b0', '#c7b0ec', '#b0ecc7']  

#setting up figure (Forgot this and suffered)
fig, ax = plt.subplots(figsize=(8, 5))


clover_img = mpimg.imread("/Users/monicautashiro-aichouri/Documents/GitHub/ORCA6-Studies/scripts/clover.png")

# Plot stems (lines) and scatter
for i, (zpe, color) in enumerate(zip(zpe_values, colors)):
    ax.plot([i, i], [0, zpe], color=color, lw=2)

    # Make the clover image larger with zoom
    imagebox = OffsetImage(clover_img, zoom=0.15)  
    ab = AnnotationBbox(imagebox, (i, zpe), frameon=False)
    ax.add_artist(ab)
    # labeling each scatter
    ax.text(i + 0.1, zpe, f'{zpe:.2f} kcal/mol', ha='left', va='center', fontsize=10)


plt.xticks(ticks=range(len(functionals)), labels=functionals)
ax.set_xlim(-0.5, len(functionals) - 0.5)  # give the markers room


ax.set_xticks(range(len(functionals)))
ax.set_xticklabels(functionals)
ax.set_ylabel("Zero-Point Energy (kcal/mol)")
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()

plt.savefig("OH_freq_comparison_GS.png", dpi=300)  
plt.show()

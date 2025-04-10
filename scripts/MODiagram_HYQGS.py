import pandas as pd

mo_data=pd.DataFrame({
    "index": list(range(26,33)),
    "label":['σ', 'π', 'π', 'π*', 'π*', 'π*', 'σ*'],
    "energy_b3lyp":[-8.3057, -6.9459, -5.483, -0.2496, 0.6621, 1.3595, 1.3813] 
})

index2 = [27, 28]
energy_pbe0 = [-5.8159, -0.1811]
energy_pbe = [-4.6978, -1.0565]


x_b3lyp = 0
x_pbe0 = 2
x_pbe = 3

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(6, 8))
width, height = (0.3, 0.3)
# Rectangle((x - width/2, row["energy_b3lyp"] - height/2),width, height,facecolor='white', edgecolor='black', linewidth=1.5)

for i, energy in enumerate(energy_pbe0):
    mo_index = 28 + i
    edgecolor = '#e6c8b3' if mo_index == 28 else '#c760ec'
    rect = Rectangle((x_pbe0 - width/2, energy - height/2), width, height,
                     facecolor='white', edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(rect)

ax.text(x_pbe0, energy_pbe0[0], '⇅', ha='center', va='center', fontsize=12)


for i, energy in enumerate(energy_pbe):
    mo_index = 28 + i
    edgecolor = '#e6c8b3' if mo_index == 28 else '#c760ec'
    rect = Rectangle((x_pbe - width/2, energy - height/2), width, height,
                     facecolor='white', edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(rect)

ax.text(x_pbe, energy_pbe[0], '⇅', ha='center', va='center', fontsize=12)


for _, row in mo_data.iterrows():
    mo_index = row["index"]
    energy = row["energy_b3lyp"]

    if mo_index in [26, 27, 28]:
        edgecolor = '#ecc760'
    elif mo_index in [29, 30, 31, 32]:
        edgecolor = '#c760ec'
    else:
        edgecolor = 'black'


    if mo_index == 31:
        x = x_b3lyp - 0.15
    elif mo_index == 32:
        x = x_b3lyp + 0.15
    else:
        x = x_b3lyp

    rect = Rectangle((x - width/2, energy - height/2), width, height,
                 facecolor='white', edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(rect)

    if mo_index == 32:
        ax.text(x + 0.25, energy, row["label"], ha='left', va='center', fontsize=10)
    else:
        ax.text(x - 0.25, energy, row["label"], ha='right', va='center', fontsize=10)


    if mo_index in [26, 27, 28]:
        ax.text(x, energy, '⇅', ha='center', va='center', fontsize=12)



# HOMO Legend Box
legend_homo = Rectangle((3.2, -8.5), 0.2, 0.2, facecolor='white', edgecolor='#ecc760', linewidth=1.5)
ax.add_patch(legend_homo)
ax.text(3.42, -8.4, 'HOMO', va='center', ha='left', fontsize=10)
ax.text(3.3, -8.4, '⇅', ha='center', va='center', fontsize=10)

# LUMO Legend Box
legend_lumo = Rectangle((3.2, -8.1), 0.2, 0.2, facecolor='white', edgecolor='#c760ec', linewidth=1.5)
ax.add_patch(legend_lumo)
ax.text(3.42, -8.1, 'LUMO', va='center', ha='left', fontsize=10)


img_path = "/Users/monicautashiro-aichouri/Documents/GitHub/ORCA6-Studies/Figures/MOImages"
mo_indices = range(26, 33) 
import os
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

for _, row in mo_data.iterrows():
    mo_index = row["index"]
    energy = row["energy_b3lyp"]
    img_file = os.path.join(img_path, f'HYQ_MO{mo_index}.jpg')

    if os.path.exists(img_file):
        image = mpimg.imread(img_file)

        if mo_index == 26:
            x_img, y_img = 1.0, energy
        elif mo_index == 27:
            x_img, y_img = 1.0, energy
        elif mo_index == 28:
            x_img, y_img = 1.0, energy
        elif mo_index == 29:
            x_img, y_img = 1.0, energy - 0.5
        elif mo_index == 30:
            x_img, y_img = 1.0, energy - 0.4
        elif mo_index == 31:
            x_img, y_img = 0.8, energy
        elif mo_index == 32:
            x_img, y_img = 1.5, energy
        else:
            continue 

        offset_img = OffsetImage(image, zoom=0.4)
        ab = AnnotationBbox(offset_img, (x_img, y_img), frameon=False)
        ax.add_artist(ab)





ax.set_ylabel("Orbital Energy (eV)")
ax.set_xticks([x_b3lyp, x_pbe0, x_pbe])
ax.set_xticklabels(['B3LYP', 'PBE0', 'PBE'])
ax.set_ylim(-9, 2)
ax.set_xlim(-1, 4)


plt.tight_layout()
plt.savefig("OH_MODiagram_GS.png", dpi=300)  
plt.show()
import matplotlib.pyplot as plt

data = [1.3771, 1.377, 1.3673, 1.3672, 1.3549, 1.3549,
         1.3549, 1.3549, 1.3549, 1.3549, 1.3717, 1.3712,
           1.3712, 1.3699, 1.3699, 1.357]
labels = ['BLYP', 'BLYP and def2/J + RI on', 'PBE', 'PBE and def2/J + RI on', 
          'PBE0', 'PBE0 + RIJCOSX', 'PBE0 + RIJK', 'B3LYP', 'B3LYP + RIJCOSX', 'B3LYP + LIBXC', 
          'TPSS', 'TPSS + D3BJ', 'TPSS + LibXC', 'BP86', 'BP86 + RIJCOSX',  'B97M-D3BJ + def2/J']

group_boundaries = [2, 4, 7, 10, 13, 15]


color1 = [0, 2, 4, 7, 10, 13, 15]
colors =['#ecc7b0' if i in color1 else "#c7b0ec" for i in range(len(data))]


x = []
spacing = 0
for i in range(len(data)):
    x.append(i + spacing)
    if i + 1 in group_boundaries:
        spacing += 1

plt.figure(figsize=(10,5))
bars = plt.bar(x, data, color=colors)

for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.0005,
             f'{data[i]:.4f}', ha='center', va='bottom', fontsize=7)
plt.xticks(ticks=x, labels=labels, rotation=75, ha='right')

plt.ylabel("Bond Length(Å)")
plt.grid(False)



plt.tight_layout()

plt.savefig("Bond_Lengths_BarPlot.png", dpi=300)
plt.savefig("Bond_Lengths_BarPlot.svg")
plt.show()


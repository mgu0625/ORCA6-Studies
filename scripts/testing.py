data = [1.3771, 1.377, 1.3673, 1.3672, 1.3549, 1.3549,
         1.3549, 1.3549, 1.3549, 1.3549, 1.3717, 1.3712,
         1.3712, 1.3699, 1.3699, 1.357]

labels = ['BLYP', 'BLYP and def2/J + RI on', 'PBE', 'PBE and def2/J + RI on', 
          'PBE0', 'PBE0 + RIJCOSX', 'PBE0 + RIJK', 'B3LYP', 'B3LYP + RIJCOSX', 
          'B3LYP + LIBXC', 'TPSS', 'TPSS + D3BJ', 'TPSS + LibXC', 
          'BP86', 'BP86 + RIJCOSX', 'B97M-D3BJ + def2/J']

highlight_indices = [0, 2, 4, 7, 10, 12]

print("Length of data:", len(data))
print("Length of labels:", len(labels))
print("Length of highlights:", len(highlight_indices))

for i in highlight_indices:
    if i >= len(data):
        print(f"⚠️ WARNING: highlight index {i} is out of range!")

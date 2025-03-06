# Post-Calculation Analysis in ORCA 6

After running ORCA 6 calculations, the next step involves visualizing molecular orbitals (MOs), electron density and vibrational modes using tools such as VMD and Chemcraft, demonstrated in this tutorial. 

This guide covers:
- Generating MO visualization files (`.cube`, `.molden`) in ORCA 6
- Using **VMD** for MO and electron density visualization
- Using **Chemcraft** for structure analysis and MO visualization

---------

## 1. Generating MO Visualization Files in ORCA 6

ORCA provides several ways to visualize molecular orbitals and electron density.

The most common formats are:
- `.cube` $\vartriangleright$ Used for MO and electron density plots in VMD
- `.molden` $\vartriangleright$ Used for MOs in Chemcraft and Molden
- Direct `.out` reading $\vartriangleright$ only supported by Chemcraft from personal testing

#### Step 1: Modify ORCA Input File to Generate MO Files

INSERT PHOTO

After running ORCA calculations, would generate the requested .cube files.

INSERT PHOTO

------

## 2. Visualizing Molecular Orbitals in VMD 

#### Step 2: Visualizing Molecular Orbitals in VMD

1. Launch VMD 
	- I use VMD on MacBook via **wine**; on Mac or Linnux, must use wine extension to work with both VMD and Chemcraft.

2. Click "File" → "New Molecule"

3. Select your ORCA ".xyz file" and click "Load" 

4. Click "Load Data" and select the ".cube" file (HOMO/LUMO)

#### Step 3: Display the MO Surface

1. "Graphics" → "Representations"

2. Set Drawing Method to "Isosurface"

3. Adjust the Isovalue to control the MO shape

4. Change Coloring Method to **"Volume"**

----------

## 3. Using Chemcraft for MO & Geometry Analysis

Chemcraft allows you to directly open ORCA **".out"** files or use **".molden"** files.
	***** I personally like to work with Chemcraft the best because a) creates most pretty figures and b) easy to work directly with .out files

#### Step 4: Open ORCA **".out"** File in Chemcraft

1. Open Chemcraft via Wine for non-Windows user

2. "File" → "Open Output File"

3. Select your ORCA output 

4. View the optimized geometry, vibrational modes, and MOs

#### Step 5: Load **".molden"** File in Chemcraft

1. Click "File" → "Open Molden File"

2. Choose the molden file

3. "Molecular Orbitals" → "Visualize MOs"

4. Select HOMO/LUMO or any MO of interest

--------

## 4. Summary & Next Steps

Generate MO visualization files (.png, .jpeg) for showcasing :)

Make sure orbitals (Isosurfaces) looks normal before proceeding to next calculations

------

Resources for Advanced post-processing:


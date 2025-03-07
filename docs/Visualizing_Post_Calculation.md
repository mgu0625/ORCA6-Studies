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

<img width="300" alt="image" src="https://github.com/user-attachments/assets/1d0cdfea-0cc3-4543-8afa-28001922b7b8" />


After running ORCA calculations, would generate the requested .cube files.

<img width="248" alt="image" src="https://github.com/user-attachments/assets/f56f0176-9fa0-4928-a786-87dac8021b7a" />


------

## 2. Visualizing Molecular Orbitals in VMD 

#### Step 2: Visualizing Molecular Orbitals in VMD

1. Launch VMD 
	- I use VMD on MacBook via **wine**; on Mac or Linnux, must use wine extension to work with both VMD and Chemcraft.

2. Click "File" → "New Molecule"

<img width="300" alt="image" src="https://github.com/user-attachments/assets/e26393a0-b110-4647-823c-447ff1636f75" />

3. Click "Browse" on new tab than select the ORCA generated ".xyz file" and click "Load" 

4. Click "Load Data" and select the ".cube" files (HOMO/LUMO, spin density, electron density, etc)

Should see molecule on "Open GL Display" Tab

<img width="300" alt="image" src="https://github.com/user-attachments/assets/80c8bf5e-082a-4313-a0a1-bce390a029e5" />


#### Step 3: Display the MO Surface

1. "Graphics" → "Representations"

2. Set Drawing Method to "Isosurface"

Select Create Rep -> Coloring Method -> Select Volume 

Select .cube file in the center (If choosing MO file, create another representation and make isovalue negative)

<img width="250" alt="image" src="https://github.com/user-attachments/assets/251f085c-80fa-4ec2-bc3d-07da433e48f2" /> <img width="250" alt="image" src="https://github.com/user-attachments/assets/584ccdb4-c9ca-4cb7-b00a-fdc295cfedce" />

<img width="250" alt="image" src="https://github.com/user-attachments/assets/636b118c-1735-488f-b3e5-e43d4a12bc3c" />

Shows (From Electron density file):

<img width="300" alt="image" src="https://github.com/user-attachments/assets/2c620f32-21d4-4196-9ed5-32a0db14e16a" />



3. Adjust the Isovalue to control the MO shape

4. Change Coloring Method to **"Volume"**

Displaying labels on atoms

Open console from VMD Main Tab

<img width="300" alt="image" src="https://github.com/user-attachments/assets/98d1ce9d-1a68-4a67-b096-a389ce9899d4" />

This script worked!

<img width="300" alt="image" src="https://github.com/user-attachments/assets/3dbd2fa2-8562-4396-9923-695e30a5b4e7" />

<img width="250" alt="image" src="https://github.com/user-attachments/assets/6da60de5-475c-4bce-943d-6cd5d39bee9d" /> <img width="250" alt="image" src="https://github.com/user-attachments/assets/e077a300-db79-47f9-bfb8-058c32fd9ae5" />



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


# Hydroquinone (HYQ) ORCA 6 Detailed Electronic Study

### 1 Hartree (Eh) = 27.2114 eV = 630 kcal/mol = 2600 kJ / mol = $2.2 x 10^5 cm^{-1}$ = 1/13.6 Bohr

### 1. Introduction & Experimental Relevance
HYQ is an aromatic organic compound with formula $C_6G_4(OH)_2$ consisting of 14 atoms. 



It is widely studied due to its redox properties, bonding capabilities, and role in various chemical and biological processes;

Commonly used for:

- **Photochemistry**: Excellent reducing agent, critical for radical chemistry
- **Electrochemistry**: Undergoes reversible oxidation to quinone
- **Spectroscopy**: Characterized via UV-vis, IR and Raman Spectroscopy
- **Solubility & Solvent Effects**: Solubility varies in different solvents, making **solvent modeling** crucial for comparison with experimental results

References for HYQ Studies:
- 10.21577/0103-5053.20170022
- 10.1039/D2NJ04878G
- 10.1021/jp200381n

-----

### Goals for Case Study
****Systematically analyze HYQ using DFT calculations in ORCA 6.****

1. Gas-Phase Structural and Vibrational Analysis
- Perform geometry optimization and frequency calculations using seven different DFT functionals.
- Compare results across Generalized Gradient Approximation (GGA), Hybrid-GGA, and Meta-GGA functionals.
- Assess influence of auxiliary basis sets on computational accuracy and efficiency

2. Solvent Effect Analysis
- Evaluate solvation effects using CPCM solvation model and CPCM with surface-type Gaussian cavity construction
- Compare structural and electronic properties of HYQ in acetonitrile, DMSO, n-hexane, and water
- Investigate the interplay between solvent and functional choice (**PBE, PBE0, B3LYP**).

3. MO and Electron Density analysis
- Extract **MO data** using different ORCA's built-in MO printing commands.
- Investigate electronic structure changes in different solvent environments.
- Visualize key orbitals using **VMD** and analyze spin density distribution.

4. TDDFT Study and Excited-State Properties
- Perform **TDDFT** calculation to obtain vertical excitation energies
- Analyze the **contributions of molecular orbitals (MOs) to each excitation**.
- Generate UV-vis spectrum from TDDFT oscillator strength
- Visualize Neutral Transition Orbitals (NTOs) to interpret electronic transitions

5. Relaxed Excited-State Geometry Optimization
- Optimize the lowest excited-state geometry using **TDDFT with state-tracking**.
- Compare changes in structural parameters between **ground and excited states**.
- Evaluate energy barriers for relaxation and identify key structural rearrangements.

6. Potential Energy Surface (PES) and Spectral Analysis
- Construct **1D, 2D, and maybe 3D PES scans** along key reaction coordinates.
- Generate **UV-Vis spectra plots** from TDDFT data.
- Create **excited-state energy diagrams** and **MO visualizations**.
- Automate PES, UV-Vis, and excited-state diagram plotting using **Python**.


------

# Step-by-Step Computational Workflow

## 1. Gas-Phase Geometry Optimization and Frequency Calculation

Functionals Used
- GGA: PBE, BLYP, BP86
- Hybrid-GGA: PBE0, B3LYP
- meta-GGA: TPSS, B97M-D3BJ

  
- Basis Set Used: def2-SVP

**Sample Input files: /ORCA6-NOTES/input_files**

Key Computational Settings:
   - **TightSCF**: Ensured more accurate SCF convergence (done by lowering energy and density error thresholds to improve electronic structure precision)
   - **VerytightOPT**: Used to apply strict optimization criteria, minimizing residual forces on atoms for highly accurate bond lengths and angles
  
#### Post-Geometry Optimization Checks
- Confirm successful termination at bottom of `.out` file.
  
<img width="300" alt="image" src="https://github.com/user-attachments/assets/4692d3a0-1eec-430a-951a-51a238e418d9" />

- Use ChemCraft (Recommended for ORCA users) or other software (Avogadro, VMD, MacmolPlt etc.,) to visualize optimized structures

- Values to extract:
  	- $E_{final}$ (Final SCF Energy) located towards end of ".out file"
  	  
		<img width="350" alt="image" src="https://github.com/user-attachments/assets/1a8fbf7c-d9bc-4403-8c75-be5d0217fab0" />
 
        - $E_{initial}$ is found right under where it **first** mentions SCF Converged
  	 
       <img width="400" alt="Screenshot 2025-03-03 at 9 05 24 PM" src="https://github.com/user-attachments/assets/c297f681-8743-4bac-a403-46be79979dc4" />

	-  ΔE (in eV) was computed as: $ΔΕ(eV) = (Ε_{functional} - E_{lowest}) x 27.2114 = (E_{f} - E_{i})$

       	- Python Script (attached to /script) was used to extract bond lengths and RMSD
  	    	- automated by parsing .xyz file to find the optimized coordinate and to reference for evaluating structural deviation (Make sure to know Atom Numbers, can visualize using Avogadro)


##### From Geometry Optimization of HYQ at Gas-Phase (Comparison of Functionals)
| Functional Name | Aux Basis | Final SCF Energy (Hartree) | ΔE (eV) | Computational Time |
| :---: | :---: | :---: | :---: | :---: |
| BLYP | none | -382.2830706 | -0.313556003 | 2 min 8.769 sec | 
| --- | def2/J + RI on | -382.2834179 | -0.313309135 | 55.29 sec |
| PBE | none | -381.9640679 | -0.304378283 | 2 min 20.10 sec |
| --- | def2/J + RI on | -381.9644084 | -0.304163873 | 56.142 sec |
| B3LYP | none | -381.9829343 | -0.267288528 | 2 min 15.324 sec |
| --- | def2/J + RIJCOSX | -381.9832893 | -0.267177549 | 4 min 2.50 sec |
| --- | def2/J + LibXC | -382.1967823 | -0.255921052 | 3 min 58.418 sec |
| PBE0 | none | -381.9829343 | -0.267288663 | 2 min 13.679 sec |
| --- | def2/J + RIJCOSX | -381.9832893 | -0.267177594 | 3 min 57.690 sec |
| --- | def2/J + RIJK | -381.9828504 | -0.267396184 | 1 min 39.645 sec | 
| BP86 | none | -382.420062 | -0.305415524 | 2 min 21.268 sec |
| --- | def2/J + RIJCOSX | -382.420062 | -0.305415524 | 57.28 sec |
| B97M-D3BJ | def2/J + RI on | -382.6225074 | -1.16304756 | 1 min 9 .722 sec |


##### Findings from Geometry Optimization
- Best Functional:
  	- Best ΔE which is the lowest reported was B3LYP + LibXC being -0.256 eV
  	- Second best was PBE0 with RIJK (better approximation compared to RIJCOSX) with ΔE being -0.2674 eV for RIJK used and -0.2672 eV for RIJCOSX used

- Worst Functional:
  	- meta-GGAs, yielded large |ΔE|, showcasing significant shift and suggesting overestimated stabilization.

- Computational Cost vs Accuracy:
  	- Some basis sets converged faster but most likely sacrificed accuracy.
  	- RIJCOSX-based hybrid-GGA functionals (e.g., PBE0, B3LYP) showed more accuracy HOWEVER, required longer computational times.
  	- def2/J + RI on sets optimized under a min while using RIJCOSX increased computational time to under 5 minutes.
  	- RIJK computed faster compared to RIJCOSX (PBE0) even though RIJK is more computationally expensive

#### Vibrational Frequency Analysis
- vibrational frequencies (towards bottom of `.out`) were checked to make sure there's no imaginary frequencies

<img width="300" alt="image" src="https://github.com/user-attachments/assets/386be11e-0a6f-4b74-96c7-7990f1027027" />

- Zero Point Energy (ZPE) correction found towards bottom of `.out` file

  <img width="300" alt="image" src="https://github.com/user-attachments/assets/a1d3c88e-e20a-4383-80df-afab1f241e28" />

- Recorded $ΔΗ_{corr}$, $ΔG_{corr}$ and ΔS values

| Functional Name | Aux Basis | ΔE(eV) | Final SCF Energy (Eh) | ZPE (kcal/mol) | $ΔΗ_{corr}$ (Eh) | $ΔG_{corr}$ (Eh) | $ΔS_{final}$ (kcal/mol) | Computational Time |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| PBE0 | def2/J + RIJCOSX | -4.56349E-08 | -381.9832893 | 68.98 | -381.8657428 | -381.9038059 | 23.88 | 3 min 56.668 sec |
| B3LYP | RIJCOSX + LIBXC | -6.33209E-08 | -382.1967823	| 68.25 | -382.0803708 | -382.1184962 | 23.92 | 3 min 51.463 sec | 
| PBE | def2/J + D3BJ | -0.278910525 | -381.9746582 | 2.51 | -381.8607585 | -381.8990914 | 24.05 | 1 min 25.441 sec |


##### Key Observations from Frequency Calculations
- B3LYP showed the most stable energy with the lowest final SCF energy (-382.197 Eh), suggesting better stabilization than PBE0.
- PBE showed the least stable energy structure with the highest final SCF energy (-381.861 Eh), suggesting less stable electronic structure
- PBE showed highest ZPE energy, indicating inadequate vibrational scaling or missed contributions (most likely from an Error of attempting to use D3BJ with parameters).
- Corrected $ΔΗ_{corr}$ and $ΔG_{corr}$ followed trend of B3LYP > PBE0 > PBE, reinforcing B3LYP's stronger stabilization
- Similar $ΔS_{final}$ indicate similar vibrational contributions across all functionals.
- B3LYP overall showed most thermodynamically stable functional for this system with PBE0 being comparatively stable but with slightly less stability as indicated by higher energies.


##### Dispersion Correction Issues (PBE + D3BJ)
- Error when attempting to use D3BJ Dispersion Correction with PBE functional (Following DOI: 10.1063/1.4907719 and DOI: 10.1021/acs.jpclett.6b00780)
-Possible cause: ORCA's limited support for D3BJ with PBE despite specifying parameters in input file.
- PBE is pure DFT and ORCA typically applices D3 for pure GGA functionals [Read About it More](https://www.faccts.de/docs/orca/6.0/manual/contents/detailed/model.html)

From `.out` file 

<img width="350" alt="image" src="https://github.com/user-attachments/assets/0560e288-487b-4fe9-9e8f-9c54cd5e3071" />


Plotting IR Spectrum (using EXCEL)

| From 0 to 2000 $cm^{-1}$ | From 0 to 500 $cm^{-1}$ |
| :---: | :---: |
| <img width="350" alt="image" src="https://github.com/user-attachments/assets/b3816504-659f-49e0-bf13-886255b8f2c1" /> | <img width="300" alt="image" src="https://github.com/user-attachments/assets/86c7ae69-1271-4d1b-8ec7-aa878963fa48" /> |

------------

## 2. Solvent Effect Analysis

### Computational Setup

Solvent Implementation:
- **CPCM(SolventName)** was used, with dielectric constant specified under `%cpcm`
- `surface_type Gaussian` was tested to determine solvent cavity construction impact.
  

##### Solvent Considered for HYQ Calculations:
- Acetonitrile (Polar Aprotic Solvent)
- Water (Polar Protic Solvent)
- DMSO (Polar Aprotic Solvent) 
- n-Hexane (NonPolar Solvent)

**Example input file in /ORCA6-NOTES/input_files/HYQ_GeomOpt_CPCM_PBE0.inp**

### Geometry Optimization Results

| Functional Name | Solvent | Final SCF Energy (Hartree) | ΔE (eV) | Computational Time |
| :---: | :---: | :---: | :---: | :---: |
| B3LYP | Acetone | -382.208227388075 | -0.241367096 | 4 min 14.320 sec |
| --- | DMSO | -382.2113271 | -0.241297194 | 4 min 14.413 sec |
| --- | Hexane | -382.2033213 | -0.248398331 | 4 min 15.613 sec | 
| --- | Water | -382.2114998 | -0.241175968 | 4 min 16.740 sec | 
| PBE0| Acetone | -381.9986297 | -0.248162775 | 4 min 31.259 sec |
| --- | DMSO | -381.9987252 | -0.248079807 | 4 min 58.527 sec |
| --- | Hexane | -381.9902326 | -0.257536544 | 4 min 14.743 sec |
| --- | Water | -381.9989082 | -0.247910611 | 8 min 55.153 sec |
| PBE | Acetone | -381.989019 | -0.381402812 | 1 min 13.173 sec |
| --- | DMSO | -381.989109 | -0.568711078 | 1 min 13.914 sec |
| --- | Hexane | -381.981134 | -0.575499805 | 1 min 8.644 sec |
| --- | Water | -381.9892816 | -0.568597143 | 1 min 13.496 sec |

##### Key Observations from Geometry Optimization Results
- B3LYP & PBE0 results yielded similar ΔE values across solvents (0.241–0.257 eV), indicating minimal structural impact from solvation
- PBE displayed large ΔE shifts, particularly in DMSO (~0.569 eV), and water (~0.568 eV), suggesting poor solvation modeling
- Non-polar n-hexane generally resulted in less stabilization across all functionals due to higher SCF energy observed.
- PBE0 was the slowest functional, especially in water (~9 min) due to complex solvation interactions.

### Frequency Calculation Results

| Functional Name | Solvent | Final SCF Energy (Hartree) | ΔE (eV) | ZPE (kcal/mol) | $ΔΗ_{corr}$ (Eh) | $ΔG_{corr}$ (Eh) | $ΔS_{final}$ (kcal/mol) | Computational Time |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| B3LYP | Acetone | -382.2112371 | 272611.5679 | 68.15 | -382.095113 | -382.1330766 | 23.88 | 4 min 31.176 sec |
| --- | DMSO | -382.2113271 | 272611.6321 | 68.15 | -382.095113 | -382.1331676 | 23.88 | 4 min 30.689 sec |
| --- | Hexane | -382.2033214 | 272605.9222 | 68.21 | -382.0869864 | -382.1250861 | 23.91 | 4 min 31.679 sec |
| --- | Water | -382.2114998 | 272611.7553 | 68.15 | -382.0952886 | -382.133342 | 23.88 | 4 min 32.873 sec |
| PBE0 | Acetone | -381.9986297 | 272459.926 |	68.86 | -381.8813292 | -381.9193066 | 23.83 | 4 min 1.376 sec |
| --- | DMSO | -381.9987252 | 272459.9942 | 68.86 | -381.8814265 | -381.9194032 | 23.83 |4 min 24.306 sec |
| --- | Hexane | -381.9902326 | 272453.937 | 68.93 | -381.8727854 | -381.9108157 | 23.86 | 4 min 20.503 sec 
| --- | Water |	-381.9989082 | 272460.1247 | 68.86 | -381.8816131 | -381.9195885 | 23.83 | 4 min 23.636 sec |
| PBE| Acetone | -381.989019 | 272437.7667 | 66.52 | -381.8752856 | -381.913542 | 24.01 | 2 min 40.605 sec |
| --- | DMSO | -381.989109 | 272445.5524 | 66.52 | -381.8753775 | -381.9136338 | 24.01 | 1 min 37.322 sec |
| --- | Hexane | -381.981134 | 272439.8597 | 66.57 | -381.8672963 | -381.9055993 | 24.04 | 1 min 37.127 sec |
| --- | Water | -381.9892816 | 272445.6756 | 66.52 | -381.8755527 | -381.9138079 | 24.01 | 1 min 37.147 sec |

##### Key Observations from Vibrational Frequency Results using CPCM
- ZPE remained consistent across solvents (~68 kcal/mol for B3LYP/PBE0 ~66 kcal/mol for PBE).
- $ΔΗ_{corr}$ and $ΔG_{corr}$ followed functional stability trends:
  - B3LYP > PBE0 > PBE in all solvents, reinforcing $$B3LYP$$’s better at solvation modeling. 
- Entropy values ($S_{final}$) were stable, suggesting minimal solvent influence on vibrational modes.
- Water and DMSO led to the most stable electronic structures (lowest SCF energy), while n-hexane consistently resulted in higher energy states.

### Conclusion from Solvent Analysis

Solvent Impact on Energy:
- **B3LYP** and **PBE0** showed consistent SCF energies across solvents, indicating reliable solvation treatment.
- **PBE** struggled in polar solvents (DMSO & Water), producing large ΔE shifts, highlighting potential inaccuracies in solvation modeling.
- Non-polar solvents (n-hexane) lead to less stabilization across all functionals.

Vibrational & Thermodynamic Properties:
- Minimal solvent dependence on ZPE, entropy, and $ΔΗ_{corr}$ trends
- **B3LYP** provided most stable vibrational corrections across all solvents

Computational Cost vs Accuracy:
- **PBE** was fastest (~1-2 min) but showed inaccuracy in polar solvents.
- **B3LYP** and **PBE0** required ~4-9 min but delivered better stability and solvation treatment.

🏆 Best Functional & Solvent Choice for HYQ 🏆

Functional Winner: B3LYP       Solvent Winner: DMSO (Polar Aprotic)

-----------

## 3. Electronic Structure Analysis

#### MO Data Extraction
- Single-Point energy calculation was performed to generate MO information.
- Example ORCA Input Keyword:
  	- `! RKS def2-SVP RIJCOSX LIBXC(B3LYP) TightSCF PrintBasis`
 
**Example Input File for running Single Point Energy + plotting request: '/ORCA6-Studies/input_files/HYQ_B3LYP_SPEnergy.inp'**

From Output File:

<img width="400" alt="image" src="https://github.com/user-attachments/assets/a4b24d87-a344-4304-9ebc-1b4fe34ec194" />


- Generating MO cube Files to visualize (Under %plots):

<img width="342" alt="image" src="https://github.com/user-attachments/assets/e96df517-2bdd-4aaf-ab43-014629f810bd" />

From Output File:
  
<img width="250" alt="image" src="https://github.com/user-attachments/assets/c2ebb716-2cbf-46f2-b6f5-307bafa82ef0" />

- Gas-phase .xyz file (from frequency calculation using same functional) was used as reference geometry.

- Also tested split-basis set (def2-TZVP basis set for O atoms)

<img width="250" alt="image" src="https://github.com/user-attachments/assets/afbbb6d5-d94e-447b-948b-71e9c08c1461" />


#### MO Visualization in VMD
1. Load `.xyz` structure (from gas-phase calculation) as a new molecule.
2. Overlay `.cube` files as a visualization state to inspect MO surfaces.
3. Adjust isosurface levels, background, and bond thickness to improve clarity.

**Key Visualizations**

Spin Density of HYQ (visualized on VMD)

<img width="300" alt="image" src="https://github.com/user-attachments/assets/12fb790c-4484-4ba5-8961-cc5715dcec8a" />

| MO #29 (HOMO) |  MO #30 (LUMO) |
| :---: | :---: |
| <img width="200" alt="image" src="https://github.com/user-attachments/assets/b3943210-f067-42d5-a5e7-1275f958519e" /> | <img width="200" alt="image" src="https://github.com/user-attachments/assets/49f39231-ee9d-437b-95ae-8ef61015b13e" /> |

#### Key Observations:
- HOMO: Primarily located on center aromatic ring carbons
- LUMO: Shows electron density on the ring as well as one side of the hydroxide group (could be on other side as well but appears "sliced").
- Spin Density: showed homogeneous spin density throughout the molecule but appeared sliced on the same Oxygen (Oxygen #2 on .xyz file) as shown on the HOMO LUMO MOs

#### Troubleshooting Notes:
- Isosurfaces appeared sliced at default values.
	- Adjusted isosurface to 0.5—resolved slicing issue.
	- Re-ran cube file generation with different dimensions but saw no improvement.
- Atom labels were difficult to display through isosurfaces.
	- Attempted Tk Console commands but removed labels due to visibility issues.
	- Verified atom correspondence using .xyz file instead.

#### Takeaways:

Solvent Effects on MO Energies:
- Compared HOMO-LUMO gap across solvents to examine stabilization effects.
- DMSO & Acetonitrile showed stronger MO stabilization compared to gas-phase and n-hexane.
  
Spin Density Observations:
- More delocalized spin distribution in polar solvents, indicating greater solvation effects.
- Non-polar environments showed localized density, suggesting weaker solute-solvent interactions.

  --------

## 4. TDDFT Analysis

#### Vertical Excitation Energy Analysis

Excited-state properties extracted from ORCA TDDFT calculations:
- Excitation energies (eV & $cm^{-1}$)
- Dominant MO contributions (e.g., HOMO → LUMO Transitions)
- Oscillator strength (fosc) for UV-vis spectral intensities.
 
Extracted TDDFT Data Available in: /HYQ/

### Sample Excitation Data:
  
| State | State	Energy (Eh) | Energy (eV) | Energy ($cm^{-1}$) |
| :---: | :---: | :---: | :---: |
| 1 | 0.162544 | 4.423 | 35674.2 |
| 2 | 0.210737 | 5.734 | 46251.3 |
| 3 | 0.228764 | 6.225 | 50207.9 | 
| 4 | 0.231882 | 6.31 | 50892.1 |

Plotted vertical excitation energy using Python Script

**Script example: `/ORCA6-Studies/scripts/jablonskiplotting.py`**

<img width="350" alt="image" src="https://github.com/user-attachments/assets/deedbe08-d4b7-4f14-829f-ad36d3e36abd" />


#### UV-Vis Spectrum Generation

Extracted TDDFT excitation wavelengths and oscillator strengths (fosc) to generate UV-vis absorption spectrum

**Python Script: `/orca6-study/scripts/uvvisplotting.py`**

Features of Python Script:
- Read TDDFT excitation data from `.xlsx`.
- Applies Gaussian broadening to simulate spectral envelope.
- Inverts x-axis (standard UV-vis convention).
- Saves spectrum as `.png` file

Running script: `python filename.py`

Generated UV-Vis Plot:

<img width="400" alt="image" src="https://github.com/user-attachments/assets/55901ecf-c399-4780-896a-ac04ea01954a" />

#### NTO (Natural Transition Orbitals) analysis

Purpose: to help visualize electronic density changes in electronic excitations.

In Input File: 

<img width="130" alt="image" src="https://github.com/user-attachments/assets/68450871-f0e2-40d5-89b8-9edd46d1f764" />

Output file Result:

<img width="200" alt="image" src="https://github.com/user-attachments/assets/c40ffc60-41d9-4d24-95c5-b7a6783e2eeb" />

Struggles here:
- Tried to use bash script to convert .nto files to .cube files but was not successful..
  	- Resulted in printing inidividual MOs from orca_plot instead 🫠
- NTO values was (probably) too small, couldn't open .cube file on VMD, ChemCraft, nor Multiwfn 🥲
	- tried redoing NTO with relaxed ES geometry optimization.

#### Takeaway
- Obtained excited-state properties from TDDFT calculations.
- Generated molecular UV-vis absorption spectrum from oscillator strengths.
- Attempted NTO visualization, but encountered issues with .cube file conversion.
	- possible the NTO energy values were too small..?

-----

## 5. Relaxed-ES Geometry Optimization

### Key Observations from CI vs TDDFT

Excitation Energies & Wavenumbers:
- Both CI and TDDFT results are identical in energy (eV) and wavenumber ($cm^{-1}$), confirming consistency in excited-state energies.
  	- Can suggest both methods are capturing similar electronic states for HYQ, validating accuracy of TDDFT.
 
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/3536f8ba-4815-4b60-9adb-710d1fde90ee" />

Final SCF Energy & Dipole Magnitude:
- SCF energies are the same in both methods. This indicates both approaches stabilize to the same electronic configuration.
- Dipole moment (3.7767 Debye) is also identical, suggesting that the electronic density distribution does not change significantly between methods.

Computation Time:
- CI: 12 min 38 sec vs. TDDFT: 12 min 37 sec
- Computational costs are nearly the same, indicating that CI does not offer a significant efficiency advantage over TDDFT for this system.

**Why I continued with TDDFT**
- More widely validated for geometry optimization and trying to keep theory consistent.

  ### Key Observations from Structural Analysis

  Ground vs. Excited-State Geomtry (Bond Lengths)

Bond Labels (`.xyz` file opened on Avogadro)
  <img width="385" alt="image" src="https://github.com/user-attachments/assets/b64a3bd1-d925-426f-9a73-25c15cbeffb9" />

#### Bond Lengths Comparison

| States | Bond Type | Bond Lengths (Å) | Bond Type | Bond Angles | Bond Type | Dihedral Angle |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| S0 | O#1 - C13 | 1.353 | C#3 - O#1 | 110.43° | C#3 - O#1 - O#2 - C#8 | -0.51° |
| - | O1 - H14 | 0.973 | C8 - O2 | |110.51° | - | - |
| - | O2 - C8 | 1.354 | - | - | - | - |
| - | O2 - H9 | 0.973 | - | - | - | - |
| S1 | O1 - C13 | 1.353 | C3(3) - O1(1) | 110.43° | C3 - O1 - O2 - C8 | -0.51° |
| - | O1 - H14(14) | 0.973 | C8(8) - O2(2) | 110.51° | - | - |
| - | O2 - C8 | 1.354 | - | - | - | - |
| - | O2 - H9 | 0.973 | - | - | - | - |			
| S2 | O1 - C13 | 1.353	 | C3 - O1 | 110.43° | C3 - O1 - O2 - C8 | -0.52° |
| - | O1 - H14 | 0.973 | C8(8) - O2 | 110.50° | - | - |
| - | O2 - C8 | 1.354 | - | - | - | - |
| - | O2 - H9 | 0.973 | - | - | - | - |
| S5 | O1 - C13 | 1.366 | C3 - O1 | 110.23° | C3 - O1 - O2 - C8 | -2.03° |
| - | O1 - H14 | 0.979 | C8 - O2 | 110.17° | - | - |
| - | O2 - C8 | 1.366 | - | - | - | - |
| - | O2 - H9 |	0.978 | - | - | - | - |
| T1 | O1 - C13 | 1.353 | C3 - O1 | 110.43° | C3 - O1 - O2 - C8 |  -0.51° |
| - | O1 - H14 | 0.973 | C8 - O2 | 110.51° | - | - |
| - | O2 - C8 |	1.354 | - | - | - | - |
| - | O2 - H9 |	0.973 | - | - | - | - |
| T2 | O1 - C13 | 1.353 | C3 - O1 | 110.43° | C3 - O1 - O2 - C8 | -0.52° |
| - | O1 - H14 | 0.973 | C8 - O2 | 110.50° | - | - |	
| - | O2 - C8 |	1.354 | - | - | - | - |
| - | O2 - H9 |	0.973 | - | - | - | - |
| T5 | O1 - C13 | 1.366 | C3 - O1 | 110.23° | C3 - O1 - O2 - C8 | -2.03° |
| - | O1 - H14 | 0.979 | C8 - O2 | 110.17° | - | - |
| - | O2 - C8 | 1.366 | - | - | - | - |
| - | O2 - H9 | 0.978 | - | - | - | - |

#### Key Observations

**Ground vs Excited-State Geometry (Bond Lengths)**

C-O bond lengths:
- S0 → S1/2/T1/T2:
  	- The O1-C13 and O2-C8 bonds remain constant (1.353 - 1.354 Å) in these states.
- S5 and T5:
	- Significant elongation of O1-C13 and O2-C8 bonds (~1.366 Å) compared to the ground state (S0, 1.353 Å).

O-H Bond Lengths:
- Stable at 0.973 Å for S1, S2, T1, T2, but slightly increases (0.979 - 0.978 Å) in S5/T5.
- Suggests weaker O-H bonding in higher excited states, potentially hinting at hydrogen bond effects or proton transfer tendencies.

**Bond Angle Trends**

C3-O1 and C8-O2 Angles:
- S0, S1, S2, T1, T2: Consistent (~110.43° - 110.51°) → Minimal structural rearrangement.
- S5/T5:
  	- Angles shift to ~110.23° and 110.17°, respectively.
  	- This could indicate partial relaxation and distortions in the higher excited states.

Angle and Bond Distance Example (IRoot T1)

<img width="333" alt="image" src="https://github.com/user-attachments/assets/a0676f64-6184-432a-968e-fbcc60efdc1d" />


**Dihedral Angle Trends**
- Minimal change (~ -0.51° to -0.52°) in S0, S1, S2, T1, and T2.
- S5 and T5 show a larger distortion (~ -2.03°).
  	- This suggests increased torsional strain or out-of-plane movement in higher excited states.

### PES
 
| 1D PES | 2D PES | 3D PES | 
| :---: | :---: | :---: |
| <img width="200" alt="image" src="https://github.com/user-attachments/assets/f28a11a8-5873-4b51-a259-d1ac6f4f4682" /> | <img width="200" alt="image" src="https://github.com/user-attachments/assets/ae57ff8c-0a0c-4023-b536-86ffe4ddca62" /> | <img width="539" alt="image" src="https://github.com/user-attachments/assets/44ce2092-c32e-43b8-a799-ee39ad568c01" /> |


---------

## 6. Potential Energy Surface (PES) and Spectral Analysis

Potential Energy Surface (PES) analysis provides insights into molecular energy variations as a function of geometric changes. This is crucial for understanding reaction pathways, excited-state behavior, and transition state dynamics.

### Generating PES Data from TDDFT

Attempted to generate PES on Python and on Matlab for S1 and T1 (Script attached) but the data was too close in numbers, the PES ended up as linear plot.

Matlab Plot

<img width="400" alt="image" src="https://github.com/user-attachments/assets/f1dfce16-50b7-40a4-b625-41796472a691" />

Possible Issues:
- Grid interpolation errors
  	- attempted to resolve by adding more unique bond lengths and using 'natural' interpolation.
- Sharp jumps in PES surface
  	- Fixed by normalizing energy to eV.
- Data points were initially too collinear, matlab refused to plot


-----

License

© 2024 Monica Utashiro-Aichouri. This work is licensed under the MIT License.
Permission is granted to use, modify, and distribute this document with attribution.

# Hydroquinone (HYQ) Computational Case Study

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

- Evaluate solvation effects using CPCM solvation model and CPCM with surface-type Gaussian
- Compare structural and electronic properties in acetonitrile, DMSO, n-hexane, and water
- Conduct calculations using PBE, PBE0, and B3LYP functionals to examine solvent and functional interplay

3. MO and NBO analysis
- Extract MO data using different ORCA's built-in MO printing commands
- Perform single-point energy calculation for NBO analysis 
- Investigate electronic structure changes in different solvent environments

------

# Step-by-Step Computational Workflow

## 1. Gas-Phase Optimization and Frequency Calculation

Functionals Used
- GGA: PBE, BLYP, BP86
- Hybrid-GGA: PBE0, B3LYP
- meta-GGA: TPSS, B97M-D3BJ

Basis Set Used: def2-SVP

**Sample Input files in /ORCA6-NOTES/input_files**

Things to Note:
   - **TightSCF**: Used to ensure more accurate SCF convergence by reducing the energy and density error thresholds, resulting in a more precise electronic structure calculation.
   - **VerytightOPT**: Used to impose stricter convergence criteria on optimization calculation, ensuring minimal residual forces on atoms and resulting in a highly optimized structure with accurate bond lengths and angles/
  
#### After Calculation
- Check bottom of `.out` file to ensure calculation terminated
  
	<img width="509" alt="image" src="https://github.com/user-attachments/assets/4692d3a0-1eec-430a-951a-51a238e418d9" />

- Use ChemCraft (Reccommended for ORCA users) or other visualizing software (Avogadro, VMD, MacmolPlt etc.,) to visualize optimized structures

- Takeaways from HYQ calculation:
  	- ΔE (in eV) was calculated as: $ΔΕ(eV) = (Ε_{functional} - E_{lowest}) x 27.2114 = (E_{first reported in .out} - E_{final single point energy})$
  	- $E_{final}$ located towards botton of .inp
  	  
  	  <img width="615" alt="image" src="https://github.com/user-attachments/assets/1a8fbf7c-d9bc-4403-8c75-be5d0217fab0" />
       	- Python Script (attached to /script) was used to extract bond lengths and RMSD
  	    	- automated by parsing .xyz file to find the optimized coordinate and to reference for evaluating structural deviation (Make sure to know Atom Numbers, can visualize using Avogadro)


**Sample `.out` files in /ORCA6-NOTES/output_files**

##### From Geometry Optimization of HYQ at Gas-Phase (Comparison of Functionals
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

- Best Functional:
  	- Best ΔE which is the lowest reported B3LYP + LibXC being -0.256 eV
  	- Second best was PBE0 with RIJK (better approximation compared to RIJCOSX) withΔE being -0.2674 eV for RIJK used and -0.2672 eV for RIJCOSX used

- Worst Functional:
  	- meta-GGAs, gives large |ΔE|, showcasing significant shift.

- Computational Cost vs Accuracy:
  	- Some basis sets converged faster but most likely sacrificed accuracy.
  	- RIJCOSX-based hybrid-GGA functionals (e.g., PBE0, B3LYP) showed more accuracy HOWEVER, required longer computational times.
  	- def2/J + RI on sets optimized under a min while using RIJCOSX increased computational time to under 5 minutes.
  	- RIJK computed faster compared to RIJCOSX (PBE0) even though RIJK is more computationally epensive


## 2. Solvent Effect Analysis

CPCM Solvation Model Calculation
- Make sure to put CPCM(solventname) next to keyword and specify dielectric constant under `%cpcm`

**Example input file in /ORCA6-NOTES/input_files**

### After Calculation
- Compare structural differences in different solvents
- Extracted dipole moments from `.out` file

    

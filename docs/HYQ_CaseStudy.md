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

1. Gas-Phase Optimization and Frequency Calculation


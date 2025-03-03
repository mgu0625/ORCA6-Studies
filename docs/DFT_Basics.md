
# **Useful Resources:**
    - **Dr. Frank Nesse**, Introduction to Quantum Chemical Methods: [YouTube](https://www.youtube.com/watch?v=-ThgCJgsi_s&t=302s)
    - **Dr. Chris Cramer**, DFT Lecture Series: [YouTube](https://www.youtube.com/watch?v=ofyr1GyEZsU&list=PL_SubSFAvBX6041nSsQUdpcDOE9MoLc4d)
    - ORCA Library [Link](https://sites.google.com/site/orcainputlibrary/home)
    - ORCA 6 Manual [Link](https://www.faccts.de/docs/orca/6.0/manual/)
    - ORCA Forum [Link](https://orcaforum.kofo.mpg.de/app.php/portal )

------
## Important things to consider when doing Computational work
    - “Always be critical of your results because in the end of the day the answer will always come from experiment” -Dr. Nesse
    - “People solve problems” aka “do not trust blind calculations” – Dr. Nesse
    - Rely on the ORCA Library and the ORCA 6 Manual, they will be your best friends through the process. Just the sections that is necessary, use CTRL + F or the search bar on the ORCA websites.
    - There is an ORCA forum in case there’s a problem in which the manual or other forums were not helpful, MPI team is very responsive.

----
## When DFT is Necessary and Useful
    - Electronic Structure Calculations: to determine MOs, spin-states and electronic configurations
    - Reaction Mechanisms: Models TS, ΔEa and reaction pathways
    - Spectroscopy Predictions: Simulate UV-Vis, IR, Raman, NMR, and EPR spectra
    - Material Science and Catalysis: Investigate Surface Interactions, Band Gaps, and absorption energies
    - Thermodynamic Properties: Calculates enthalpy, entropy, Gibbs free energy, and binding energies

 ----
## Best Systems to work on:
    - Transitional Metal Complexes: Effectve for ligand field analysis, spin states, and redox chemistry (Dr. Nesse has AMAZING videos on this)
    - Organic Molecules: Useful for electronic structure, rxn barriers, and conformational analysis
    - Periodic Systems: Suitable for semiconductors, metals and surfaces with plane-wave basis sets.
    - Weakly correlated Systems: Performs well for non-strongly correlated molecules with moderate electron delocalization

----
## Limitations of DFT:
    - Accurately Depends on Functional Choice: Struggles with dispersion, self-interaction errors, and delocalization errors
    - Proof for strongly correlated systems: Fails for transitional metals with multi-reference character
    - Limited ES Calculations: TDDFT works for singlet states but struggles with double excitations and charge transfer
    - Computational Cost: Scales poorly for very large systems compared to semi-empirical or force fields methods
    - Relies on Approximate Exchange Correlation Functionals: No universal functional, requiring empirical tuning

----
## System Sizes:
    - Small System: 1-20 atoms
    - Medium System: 20-100 atoms
    - Large System: 100+ atoms

----
## Choosing Functionals: [Helpful Link](https://sites.google.com/site/orcainputlibrary/dft-calculations)
    - Definition: Functionals in DFT are mathematical expression that approximates the exchange-correlation energy, EXC which accounts for electron-electron interactions.
    - Functionals are categorized based on complexity and accuracy, progressing from Local Density Approximation (LDA) → Generalized Gradient Approximation (GGA) → meta-GGA → hybrid GGA etc

**** For this tutorial, GGA, meta-GGA and hybrid-GGA will be used to calculate Geometry Optimization and Frequency calculation to compare energy values. 

----
## Choosing Basis Sets: Depends mainly on balance between accuracy and computational cost. 
[Helpful Link](https://sites.google.com/site/orcainputlibrary/basis-sets)

- def2 basis sets (standard choice, good for balance of accuracy and cost)
    - def2-TZVP: Best for Geometry Optimization, electronic structure, and rxn barriers with good accuracy
    - def2-SVP: less accurate compared to TZVP but much faster
- Ones better than the def2 basis ets:
    - cc-pVTZ (Correlation-Consistent triple-zeta): more accurate for thermochemistry and electron correlation effects
    - cc-pVTZ: adds diffuse functions, useful for anionic or excited-state calculations
- Cheaper alternative (A lot of paper’s and a popular 1st step approach)
    - 6-31G: less accurate but useful for medium-sized molecules

----
## RI (Resolution of Identity) and Auxiliary Basis Sets for DFT Calculations:
[Helpful Link](https://sites.google.com/site/orcainputlibrary/basis-sets/ri-and-auxiliary-basis-sets)
- RI is approximation technique that speeds up evaluation of Coulomb integrals in DFT and MP2 calculations by expanding electron density in a set of auxiliary basis set functions instead of computing for full sized integrals
- Auxiliary Basis Sets are specialized sets of functions used in RI methods to represent the electron density without directly affecting the wavefunction
- Overall makes calculations time faster and more reducing computational cost for integral calculations
- Essential for MP2 and CCSD and correlated wavefunction method where full integral evaluation is expensive

----
## VDW Dispersion Energy-Correction Term: D3BJ
- When implementing dispersion effect, make sure to assign correct parameters.
- For GGA, s6=1.0 is used
- Sources: 
    [Orca Manual](https://www.faccts.de/docs/orca/6.0/manual/contents/detailed/model.html#choice-of-functional)
    DOI: 10.1021/acs.jpclett.6b00780, DOI: 10.1063/1.3382344    

----
## Scaling of DFT Computational Time:
- Kohn-Sham DFT (Standard DFT using Gaussian Basis Sets)
	- Integrals are performed over functionals of charge density
	- Possible Ref: [Link](https://www.researchgate.net/post/How-does-a-DFT-simulation-scale-with-the-number-of-particles)
	- Time roughly scales as $N^3$ to $N^4$
	- Doubling of atoms roughly increases computational time by 8-16x
- Hybrid DFT
	- More expensive computational cost (roughly O($N^4$) to O($N^5$) due to non-local exchange interactions
	- DOI: 10.1021/acs.jctc.6b01121



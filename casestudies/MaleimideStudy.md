# Maleimide DFT Study Results

## Introduction
A detailed theoretical study was conducted on the maleimide monomer and dimer separately to investigate their electronic structure and excited-state properties. Density Functional Theory (DFT) and Time-Dependent DFT (TDDFT) calculations were performed using ORCA 6 to optimize geometries, analyze electronic transitions, and explore solvent effects.

## Computational Methods
All DFT/TDDFT calculations were performed using the def2-SVP basis set with the RIJCOSX approximation and the def2/J auxiliary basis set to improve computational efficiency. Solvent effects were incorporated using the CPCM model. Additionally, D3BJ dispersion correction was tested, though its application yielded mixed results. To improve SCF convergence, the SMD solvent model and CNVDamp were also employed.

For the maleimide dimer TDDFT calculations, initial SCF attempts with the original functional failed to converge. Based on methodological studies from prior HYQ calculations, the functional was switched to B3LYP with LibXC exchange-correlation and kinetic energy functionals. The Libint2 library was used for two-electron integral evaluations. These computational methods ensured accurate electronic structure predictions while maintaining numerical stability across different maleimide species.

## Results
#### Geometry Optimization of Maleimide Monomer

DFT calculations were performed to obtain the optimized geometry, electronic structure, and dipole moment properties. The RIJCOSX approximation was used along with the def2-basis set and CPCM solvent model (MECN) in ORCA 6.

| :---: | :---: | :---: | 
| Property | Value (Eh) | Value (eV) |
| Initial Energy $(E_i)$ | -437.30082 | -11899.567 |
| Final Energy $(E_f)$ | -437.30193 | -11899.598 |
| Dispersion Correction | -0.0133941 | — |
| ΔE (HOMO - LUMO) | — | 5.4102 |
| ΔE ($E_f$ – $E_i$) | — | 0.03022 |
| Dipole Moment Magnitude | 2.5201 Debye | — |
| Dipole Moment Energy | -437.28853 | -11899.233 |

Key Observations:
- The HOMO–LUMO gap of 5.41 eV suggests a relatively large electronic gap characteristic of stable, non-metallic systems.
- The dipole moment magnitude was calculated as 2.52 Debye, confirming a moderate polarity.

#### Vibrational Frequency Calculation of Maleimide Monomer

| :---: | :---: | :---: | 
| Property | Value (Eh) | Value (eV) |
| Initial Energy $(E_i)$ | -437.30193 | -11899.598 |
| Final Energy $(E_f)$ | -437.30193 | -11899.598 |
| Total Thermal Energy | — | -11895.977 |
| Enthalpy Correction (ΔH) | — | -11895.952 |
| Gibbs Free Energy (ΔG) | — | -11897.133 |
| Entropy (ΔS) | — | 27.23 kcal/mol |

Key Observations:
- No imaginary frequencies, confirming the system resides at a true minimum.
- The Gibbs free energy (ΔG) of -1.19 × 10⁴ eV suggests thermodynamic stability.
- The dipole moment of 2.52 Debye remains consistent.

#### Geometry Optimization of Maleimide Dimer

| :---: | :---: | :---: | 
| Property | Value (Eh) | Value (eV) |
| Initial Energy $(E_i)$ | -874.61659 | -23799.542 |
| Final Energy $(E_f)$ | -874.64365 | -23800.278 |
| Dispersion Correction | -0.0415539 | — |
| ΔE (HOMO - LUMO) | — | 6.8293 |
| ΔE ($E_f$ – $E_i$) | — | 0.03022 |
| Dipole Moment Magnitude | 4.5255 Debye | — |

Key Observations:
- HOMO–LUMO gap for dimer (6.82 eV) is larger than for monomer (5.4 eV), suggesting enhanced stability.
- The dipole moment magnitude (4.5 Debye) is nearly double that of the monomer (2.5 Debye), indicating stronger intermolecular interactions.
- Stronger dispersion in the dimer (-0.04 Eh) suggests significant Van der Waals contributions.

#### Vibrational Frequency of Maleimide Dimer

| :---: | :---: | :---: | 
| Property | Value (Eh) | Value (eV) |
| Initial Energy $(E_i)$ | -874.64365 | -23800.278 |
| Final Energy $(E_f)$ | -874.64365 | -23800.278 |
| Enthalpy Correction (ΔH) | — | -23792.858 |
| Gibbs Free Energy (ΔG) | -874.429 | — |
| Entropy (ΔS) | — | 36.45 kcal/mol |

Key Observations:
- No imaginary frequencies, confirming the system is at a true minimum.
- Higher entropy (ΔS) in the dimer (36.45 kcal/mol) compared to monomer (27.23 kcal/mol) suggests increased molecular motion.
- Gibbs free energy (ΔG) confirms thermodynamic stability.
- Dipole moment of 4.52 Debye reinforces stronger intermolecular interactions in the dimer.

<img width="411" alt="image" src="https://github.com/user-attachments/assets/7332bdcd-32f8-4e70-9d5d-7343c5b49086" />

 Infrared (IR) spectra comparison of the maleimide monomer (blue) and dimer (orange). The dimer exhibits a redshift and intensified carbonyl stretching mode (~1854 cm-1) compared to monomer (~1843 cm-1), indicating strong intermolecular interactions.


#### TDDFT Results
TDDFT Maleimide Monomer

Three TDDFT calculations were performed on the maleimide monomer to evaluate vertical excitation energies, oscillator strengths, and the impact of computational settings on electronic transitions.

- Run 1: Conducted using the PBE0 functional with the def2-SVP basis set and RIJCOSX approximation. The def2/J auxiliary basis set was used for integral calculations. This run aimed to capture excitation energies, oscillator strengths, and triplet states, while also testing the effect of dispersion correction (D3BJ) on the excited-state properties.

- Run 2: Performed with the B3LYP functional, RIJCOSX approximation, and def2/J auxiliary basis set. This run focused on analyzing singlet-triplet transitions and exploring electronic excitations in relation to orbital character and charge distribution.

- Run 3: Utilized the PBE0 functional, maintaining the RIJCOSX approximation and def2/J auxiliary basis set. Unlike Runs 1 and 2, this calculation excluded dispersion correction (D3BJ) to examine its influence on excitation energies. Additionally, the number of excited states (NRoots) was increased to 6, and triplet states were excluded to focus solely on singlet-state electronic transitions. This approach was designed to refine the absorption spectrum prediction and improve the accuracy of oscillator strengths for UV-Vis simulations.

TDDFT Mameimide Dimer Key observations: 
- A shift in absorption features, likely due to intermolecular electronic coupling and delocalization effects.
- Changes in oscillator strengths, suggesting alterations in transition dipole moments.
- Differences in state ordering and energy spacing, which could influence photophysical properties such as intersystem crossing (ISC) and fluorescence quantum yield.

### Comparison of TDDFT Runs
- The best-performing monomer run (Run 2) was selected for comparison with the dimer calculations.
- The simulated UV-Vis absorption spectrum of Run 3 showed distinct peak shifts and intensity variations, indicating potential structural or electronic state differences affecting excitation behavior.
- Excited-state energy levels extracted from all monomer and dimer runs reveal variations in singlet (S₁, S₂, S₃) and triplet (T₁, T₂) states, which could impact the dimer's photoreactivity under UV excitation.

These results provide insight into how maleimide undergoes photodimerization, with ongoing relaxed TDDFT calculations aimed at further refining the excited-state potential energy surfaces (PES).

<img width="311" alt="image" src="https://github.com/user-attachments/assets/4bfcc001-cb4a-4908-9369-7f687429efa6" />

UV-Vis Absorption Spectrum of Monomer Runs 1 and 2 generated from TDDFT Calculation on ORCA 6 and plotted using Python.


<img width="335" alt="image" src="https://github.com/user-attachments/assets/03c3e2a5-c933-4ffd-888a-20a40448183d" />

UV-Vis Absorption Spectrum of Monomer Run 2 and Dimer generated from TDDFT Calculation on ORCA 6 and plotted using Python.


<img width="383" alt="image" src="https://github.com/user-attachments/assets/99cef482-1c01-48ec-a5b3-2e2a81789d91" />

UV-Vis Absorption Spectrum of Monomer Run 3 generated from TDDFT Calculation on ORCA 6 and plotted using Python.


<img width="313" alt="image" src="https://github.com/user-attachments/assets/3ff08dad-c6de-4c2f-be91-501a36117ded" />

Excited-State Energy Diagram for Monomer and Dimer Runs generated from TDDFT Calculation on ORCA 6 and plotted using Python.



Citation:
1.	 Neese, F. Software update: the ORCA program system, version 5.0. WIREs Comput. Mol. Sci. 2022, 12 (1), e1606. https://doi.org/10.1002/wcms.1606. 
2.	Weigend, F.; Ahlrichs, R. Balanced basis sets of split valence, triple zeta valence and quadruple zeta valence quality for H to Rn: Design and assessment of accuracy. Phys. Chem. Chem. Phys. 2005, 7, 3297–3305. https://doi.org/10.1039/B508541A. 
3.	Weigend, F. Accurate Coulomb-fitting basis sets for H to Rn. Phys. Chem. Chem. Phys. 2006, 8, 1057–1065. https://doi.org/10.1039/B515623H. 
4.	Garcia-Rates, M.; Neese, F. Effect of the Solute Cavity on the Solvation Energy and its Derivatives within the Framework of the Gaussian Charge Scheme. J. Comput. Chem. 2020, 41, 922-939. https://doi.org/10.1002/jcc.26139. 
5.	Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H–Pu. J. Chem. Phys. 2010, 132, 154104. https://doi.org/10.1063/1.3382344. 
6.	Smith, D. G. A.; Burns, L. A.; Patkowski, K.; Sherrill, C. D. Revised Damping Parameters for the D3 Dispersion Correction to Density Functional Theory. J. Phys. Chem. Lett. 2016, 7, 2197–2203. https://doi.org/10.1021/acs.jpclett.6b00780. 
7.	Marenich, A. V.; Cramer, C. J.; Truhlar, D. G. Universal solvation model based on solute electron density and a continuum model of the solvent defined by the bulk dielectric constant and atomic surface tensions. J. Phys. Chem. B 2009, 113, 6378–6396. https://doi.org/10.1021/jp810292n. 
8.	Lehtola, S.; Steigemann, C.; Oliveira, M. J. T.; Marques, M. A. L. Recent developments in Libxc - A comprehensive library of functionals for density functional theory. Software X 2018, 7, 1–5. https://doi.org/10.1016/j.softx.2017.11.002. 
9.	Valeev, E. F. Libint: A library for the evaluation of molecular integrals of many-body operators over Gaussian functions, Version X.Y.Z. http://libint.valeyev.net/.


© 2025 M.G.Utashiro. All rights reserved. This document and its contents, including computational results and analyses, are provided for educational and research purposes. Redistribution, modification, or commercial use without explicit permission from the author is prohibited. Proper citation is required when referencing this work.

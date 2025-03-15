# ORCA 6 DFT Calculations Case Studies

### This repository contains different case studies of Density Functional Theory (DFT) calculations done on ORCA 6. 

This serves as:

- A portfolio project showcasing computational chemistry skills through case study demonstrations.
- A tutorial for running ORCA 6 calculations and performing post calculation visualization using ChemCraft and VMD.
- A guide for setting up a virtual node for local ORCA computations.

--------

# Repository Contents

## 1. DFT Tutorial: Hydroquinone (HYQ) Case Study

A step-by-step tutorial demonstrating essential ORCA 6 calculations on HYQ:
- Geometry Optimization
- Vibrational Frequency Analysis
- TDDFT Excited-State Calculations
- Population Analysis and Frontier Orbitals
- Data Visualization using VMD and ChemCraft

The tutorial serves as a structured introduction to running ORCA 6 for those new to computational chemistry

## 2. Case Studies in DFT
This section includes detailed case studies applying ORCA 6 to different chemical systems:

#### 1. HYQ - Detailed Electronic Study
- Analysis of electronic structure and bonding.
- Excited-state calculations using TDDFT.
- Solvent effects using the CPCM model.

#### 2. Maleimide; 2+2  Cycloaddition Mechanistic Study
- Reaction mechanism exploration using DFT.
- Transition state (TS) calculations.
- Energy barriers and reaction coordinate analysis.

#### 3. $CuC-_4^{2-}$ - Broken Symmetry Demonstration
- Spin state, spin polarization analysis using broken symmetry DFT
- Theoretical EPR study demonstration
- Evaluation of electronic structure differences in high-spin vs low-spin states

#### 4. DIPAC - Transition State (TS) Calculation
- Saddle point optimization using TS calculations
- Vibrational frequency analysis to confirm TS
- Intrinsic Reaction Coordinate (IRS) exploration

-----

## Features & Tools
- ORCA 6 input file and job submission script setup (for local and HPC execution).
- Coordinate generation and extraction using Avogadro.
- Python & Shell scripts for automation and post-processing.
- Data visualization guide: ChemCraft, VMD, and Matplotlib for plotting results.
- Virtual node setup guide for running ORCA on a local Linux environment.

## Computational Setup
- Software: ORCA 6 (Linux version)
- Execution environments:
  - Local virtual node setup
  - Ohio Supercomputer Cluster (OSC)
 
# Acknowledgments
My primary sources for learning computational chemistry and DFT principles include:
- Dr. Frank Neese (Max-Planck-Institut für Kohlenforschung)
    - from DFT and ORCA tutorials as well as as the ORCA manual
    - [Start His Video Series](https://www.youtube.com/watch?v=-ThgCJgsi_s&t=304s)
    - [ORCA Manual](https://www.faccts.de/docs/orca/6.0/manual/)
- Dr. Chris Cramer (University of Minnesota)
    - Essentials of Computational Chemistry, Theory and Models
    - [PDFCopy](http://lqtc.fcien.edu.uy/cursos/Fq2/2009/libros/Essentials%20of%20Computational%20Chemistry%20Theories%20and%20Models%202d%20Ed%20-%20Christopher%20J.%20Cramer.pdf)
- [ORCA Library](https://sites.google.com/site/orcainputlibrary/home)

## Copyright

© 2025 M.G.Utashiro. All rights reserved.  

This repository and its contents, including tutorials and case studies, are provided for educational and research purposes. Redistribution, modification, or commercial use of this material without explicit permission is prohibited. 

ORCA is developed by Dr. Neese's Group; for official documentation and licensing, visit [https://orcaforum.kofo.mpg.de](https://orcaforum.kofo.mpg.de).
  

# Running ORCA 6 Calculations 

### This Guide Covers:
- Brief Instructions on Running calculations on **personal PC** or **HPC Clusters**
- Converting **.gbw files** for visualization
- Using **ORCA 8 Print Options** (`!PrintMOs`, `!PrintBasis`, and `!NormalPrint`)
- **Visualizing electron density** and **spin density** with `orca_plt`

For ORCA 6 Installation and Extraction, Follow Guide Posted on [ORCA WEBSITE](https://www.faccts.de/docs/orca/6.0/tutorials/first_steps/install.html)

-----

## Initiating ORCA 6 Calculations

Once ORCA is installed and extracted, make sure to run command **directly** from file in which input file is located.

**IMPORTANT**: ORCA performs calculations within this directory (Personal PC and Cluster BOTH), generating and extracting files during the process. To maintain organization and avoid clutter, it's best to keep only essential files in this folder -such as `.inp`, `.xyz` and other required files like `.gbw`-while running calculations.

#### for personal PC (bash command)
`/full/path/to/ORCAsoftware/orca /full/pathlink/to/input/filename.inp > /full/pathlink/to/input/filename.out`

### for Cluster (bash command, Submission Script example in /Inp_Files)
`ssh SubmissionScript.sh` 

------

## Input Files General Guidelines
- **Example Input Files** are stored in /Inp_Files
- Ensure **Proper Syntax** and **Formatting**, always check for typos and correct file extensions.
- Make sure **MOs (Molecular Orbitals)** are Defined Correctly with **charges** and **multiplicity** [Orca 6 Guide](https://www.faccts.de/docs/orca/6.0/manual/contents/input.html)
- Specify Required Auxiliary Files:
	- If restarting calculations or using previous results, make sure to include necessary files such as `.gbw`(wavefunction), `.xyz`(geometry), or `.hess`(Hessian). 
	- [Helpful Link](https://www.faccts.de/docs/orca/6.0/manual/contents/detailed/initguess.html)
- Optimize **Computational Resource Allocation** by using %pal to specify number of CPU cores (**ESPECIALLY** if more than 1 core is used)
	- [Guide for Running Parallel Calcs](https://www.faccts.de/docs/orca/6.0/tutorials/first_steps/parallel.html)

----

## Converting `.gbw` to `.molden` in ORCA 6

- The `.gbw` files store **wavefunction information** and are required for:
	- MO visualization
	- Proceeding Calculations
- Conversion Command:
	`orca_2mkl JUSTFILENAME -molden`
	**** Will generate `.molden.input` file, convert to `.molden` by doing `mv filename.molden.input filename.molden`
- More Guide on Visualization
	[ORCA LIBRARY](https://sites.google.com/site/orcainputlibrary/visualization-and-printing)
	[ORCA 6 Utility Program](https://www.faccts.de/docs/orca/6.0/manual/contents/detailed/utilities.html)
	[ORCA 6 using GUI](https://www.faccts.de/docs/orca/6.0/tutorials/first_steps/GUI.html)

----

## ORCA 6 Print Options

**** ORCA Provides different print levels to control output verbosity ****

1. `!PRINTMOS`
- Prints **MO(Molecular Orbital)** coefficients in `.out` file.
- Useful for checking MO contributions and having to separately import `.molden` for visualization.
- Sample Input Script
	`!UKS def2-TZVP def2/J RIJCOSX SCF PRINTMOS`

2. `!PRINTBASIS` 
- Prints **full basis sets** used in calculations.
- Useful for debugging confirmation basis set definitions.
- Sample Input Script
	`!UKS def2-SVP D3BJ SCF PRINTBASIS`

3. `!NormalPrint`
- Controls **General Output Verbosity**
- Make sure to pair with `!VeryTightSCF` for strict convergence with detailed output
- Sample Input Script
	`!UKS def2-SVP def2/J RIJCOSX TightSCF NormalPrint


-----


## Using `orca_pltvib` for Vibrational Analysis

`orca_plt` is used for:
- Visualizing **normal modes** after frequency calculation
- Generating .molden file for viewing vibrations in Molden

#### Example Usage:
- After freqnecy calculation completes, use: `orca_plt FILENAME.out`

- Open Generated .molden file in molden

----

## Using orca_mpspc for Multipole Analysis

`orca_mpspc` computes **multipole surface plots**, useful for:
	- **Electrostatic Potential (ESP)** mapping
	- **Charge Distribution Visualization**

### Example Usage:
- `orca_mpspc FILENAME.out`

---- 

## Visualizing Electron Density

1. Using `%plots` in .inp file
Add following block to ORCA .inp file:

	- This will generate `.densities` file, which can be visualized using `orca_plot`

2. Using `orca_plot` Command
- To visualizing electron density from `.gbw`
	`orca_plot FILENAME.gbw -i`
- To visualize density files
	`orca_plot FILENAME.densities -i`

 

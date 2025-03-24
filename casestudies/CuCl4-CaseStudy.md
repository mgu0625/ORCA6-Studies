# This is A Demonstrative Study as Well as Test Study of Broken Symmetry DFT Calculation 

Compound: $[CuCl_4]^{2-}$

Structure built on Avogadro

<img width="366" alt="image" src="https://github.com/user-attachments/assets/d0bd92f2-d7ce-4891-be26-ae343dc3c0d5" />

Structure built on Chemdraw

<img width="274" alt="image" src="https://github.com/user-attachments/assets/4d61a9c3-981f-4e69-af8d-10297a098258" />

## Purpose of CaseStudy
- Simulate JT distortion using ORCA 6
- Follow Broken Symmetry Calculation done on Cr(III) complex by Dr. Scarsborough.

Dr. Scarsborough Paper References:
- Scarborough, C.C., et al. Electronic Molecular Structure of the Members of the Electron Transfer Series [Cr(^tbpy)_3]^n (n = 3+, 2+, 1+, 0): An X-ray Absorption Spectroscopic and Density Functional Theoretical Study. Inorg. Chem. 2011, 50, 24, 12446–12462. DOI: 10.1021/ic201123x.
- Scarborough, C.C., et al. Scrutinizing Low-Spin Cr(II) Complexes. Inorg. Chem. 2012, 51, 12, 6969–6982. DOI: 10.1021/ic300882r.


-----

###  Why is CuCl4 A Field of Interest?

- In Spectroscopic Fields: Studying Crystal Field(CF) Theory and Jahn-Teller(JT) Distortion via its d-d transitions in Cu(II).
- In Theoretical Fields: To benchmark DFT theories, explore electron correlation effects in $d^9$ systems, and to model Ligand Field (LF) theory and molecular orbital theory (MOT) modeling as well as studying solvation effects.
- In Organic and Biochem Fields: Understanding metal ion partitioning for separations and environmental cleanup

Outside of Chemistry:
- Color-changing reaction demo for education

References:
1. Candela, M. T.; Jara, E.; Aguado, F.; Valiente, R.; Rodríguez, F. Structural Correlations in Jahn–Teller Systems of Mn³⁺ and Cu²⁺: Unraveling Local Structures through Spectroscopic Techniques. J. Phys. Chem. C 2020, 124 (41), 22692–22703. DOI: 10.1021/ACS.JPCC.0C07243.
2. Szilagyi, R. K.; Metz, M.; Solomon, E. I. Spectroscopic Calibration of Modern Density Functional Methods Using [CuCl₄]²⁻. J. Phys. Chem. A 2002, 106 (12), 2994–3007. DOI: 10.1021/jp014121c.
3. Prieto, M.; Stoll, H., Eds. Ion Partitioning in Ambient-Temperature Aqueous Systems; EMU Notes in Mineralogy, Vol. 10; Mineralogical Society of Great Britain and Ireland: London, 2011. DOI: 10.1180/EMU-notes.10.

$[CuCl_4]^{2-}$ color example:

(Link of Image)[https://www.reddit.com/r/chemistry/comments/15f58ss/tetrachlorocuprate_ii_cucl4_2_complex_in_a/]

![image](https://github.com/user-attachments/assets/ca346891-a85a-4f47-b7dd-b170249e48cc)

-------


## Compound Information

<img width="274" alt="image" src="https://github.com/user-attachments/assets/4d61a9c3-981f-4e69-af8d-10297a098258" /> 

- Not stable in air and sensitive to moisture
- electron configuration ($d^9$): $1s^22s^22p^63s^23p^63d^9$
- JT Distortion of $[CuCl_4]^{2-}: 4 Cl at 230 pm 2 Cl at 295 pm

(Read about JT Distortion)[https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Supplemental_Modules_and_Websites_(Inorganic_Chemistry)/Coordination_Chemistry/Structure_and_Nomenclature_of_Coordination_Compounds/Coordination_Numbers_and_Geometry/Jahn-Teller_Distortions#:~:text=The%20Jahn%2DTeller%20effect%20is,those%20of%20the%20equatorial%20bonds.]

-----

# Step 1. Geometry Optimization using Geometry Constraints

Initially performed GeomOpt with No Constraints



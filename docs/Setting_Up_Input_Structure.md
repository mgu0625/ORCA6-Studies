# Setting Up Molecular Structures in Avogadro for ORCA 6

This guide explains how to build a molecule in Avogadro, extract atomic coordinates, and prepare an ORCA input file using a `.xyz` file instead of manually copying coordinates each time.

-----------

## 1. Building a Molecule in Avogadro

Step 1: Open Avogadro 1 and build structure
  - I personally like Avogadro 1 >> Avogadro 2 but choose your preference, both apps work similarly :)

Left Icon for Build Mode, Mickey looking Hands to change selected bond length, Mouse to Select Specific Atoms:

<img width="250" alt="image" src="https://github.com/user-attachments/assets/a11e4e69-670a-405f-b13d-19c125f572ee" />

To Change atoms, look at the bottom left:

<img width="250" alt="image" src="https://github.com/user-attachments/assets/da22c900-e000-4b04-8449-8db3aabcfe60" />

Click "Other" to pop open periodic table to choose specific element

<img width="300" alt="image" src="https://github.com/user-attachments/assets/27872d4e-655f-444a-b1e3-efd9f7b457e0" />

HYQ 

<img width="284" alt="image" src="https://github.com/user-attachments/assets/6f03f34a-437b-4227-9a92-330b68a3416e" />

Click on bonds in "Build Mode" to change single \medblacktriangleright double \medblacktriangleright triple

<img width="200 " alt="image" src="https://github.com/user-attachments/assets/f73249da-486a-4446-9ac5-8f71f7778034" /> \medblacktriangleright <img width="200" alt="image" src="https://github.com/user-attachments/assets/45b11ac1-6929-454a-972c-255371acfbed" />

Pre-Optimized HYQ

<img width="250" alt="image" src="https://github.com/user-attachments/assets/3b265e02-691e-481a-aa1b-9bf3071c4532" />

Step 2: Optimize Structure

"Extensions" → "Optimize Geometry"

<img width="200" alt="image" src="https://github.com/user-attachments/assets/3f13f036-df9e-43c4-ac02-c607c5219bd4" />

Or Choose the E Icon, which will open a popup, click start

<img width="250" alt="image" src="https://github.com/user-attachments/assets/23e88e42-bf6b-46d8-9b70-b64a0eb82b1f" />

Optimized HYQ

<img width="250" alt="image" src="https://github.com/user-attachments/assets/70815ed0-b93f-441e-859c-554a1eedebf6" />

Things to note:
- Ensure that bond lengths and angles look reasonable.
- If needed, manually adjust atoms by clicking and dragging (for transition state geometry for example)

-------

## 2. Extracting Atomic Coordinates from Avogadro

Step 3: Generate Coordinates

"Extensions" \medblacktriangleright "ORCA" \medblacktriangleright \medblacktriangleright "Generate ORCA Input.."

<img width="250" alt="image" src="https://github.com/user-attachments/assets/fa462e0a-4b22-4837-9f98-be7912634735" />

Copy paste just the coordinates to a new texteditor file (I use TextMate for Mac, Notepad++ reccommended for Windows user)

<img width="250" alt="image" src="https://github.com/user-attachments/assets/e8a0b501-ea90-4f88-9e2c-2d0b6783546d" />

first number represents the charge of compound, second number represents the multiplicity of compound

Format for .xyz file is total atom number in line 1, comment in line 2, and the pasted coordinates start from line 3.

<img width="350" alt="image" src="https://github.com/user-attachments/assets/1ba42307-ff52-4da1-8815-79473ddbbcad" />

Save file in **same directory as .inp file** for running ORCA calculations.

----

## 3. Specifying .xyz File in .inp File

Why this is useful:
- to be able to reuse .inp file with different coordinates for similar or next step calculations

How to Specify .xyz at the bottom of .inp file

<img width="350" alt="image" src="https://github.com/user-attachments/assets/90a0656d-4c04-4c2a-b21e-95e9cde71881" />

If coordinates were directly pasted to input file (no need for .xyz file in directory if so):
<img width="350" alt="image" src="https://github.com/user-attachments/assets/cb1784de-ccf2-42c7-8e11-efba009df253" />



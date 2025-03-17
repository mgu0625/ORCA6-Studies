import os
import numpy as np
from ase.io import read

def distance(atom1, atom2):
    """Calculate the Euclidean distance between two atoms."""
    return np.linalg.norm(atom1 - atom2)

def angle(atom1, atom2, atom3):
    """Calculate the bond angle between three atoms in degrees."""
    v1 = atom1 - atom2
    v2 = atom3 - atom2
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.degrees(np.arccos(np.clip(cos_theta, -1.0, 1.0)))

def dihedral(atom1, atom2, atom3, atom4):
    """Calculate the dihedral angle between four atoms in degrees."""
    b1 = atom2 - atom1
    b2 = atom3 - atom2
    b3 = atom4 - atom3

    n1 = np.cross(b1, b2)
    n2 = np.cross(b2, b3)

    n1 /= np.linalg.norm(n1)
    n2 /= np.linalg.norm(n2)

    m1 = np.cross(n1, b2 / np.linalg.norm(b2))

    x = np.dot(n1, n2)
    y = np.dot(m1, n2)

    return np.degrees(np.arctan2(y, x))

# Prompt setup

def main():
    # asking user for .xyz file
    xyz_files = [f for f in os.listdir() if f.endswith(".xyz")]
    if not xyz_files:
        print("No .xyz files found in the current directory!")
        return
    
    print("Available .xyz files:")
    for i, file in enumerate(xyz_files):
        print(f"{i + 1}. {file}")
    
    choice = int(input("Enter the number of the file to analyze: ")) - 1
    if choice < 0 or choice >= len(xyz_files):
        print("Invalid choice!")
        return
    
    xyz_file = xyz_files[choice]
    
    # Read XYZ file
    atoms = read(xyz_file)
    positions = atoms.get_positions()
    symbols = atoms.get_chemical_symbols()

    print(f"\nAnalyzing: {xyz_file}")
    print("=" * 50)

    # **Manually Assign Indices Based on File Order :(**
    O1 = 0 
    O2 = 1  
    C8 = 7  
    C13 = 12 
    H9 = 8   
    H14 = 13 

    # Bond Length 
    print("\n🔹 Bond Lengths (Å)")
    print(f"  O1({O1+1}) - C13({C13+1}) : {distance(positions[O1], positions[C13]):.3f} Å")
    print(f"  O1({O1+1}) - H14({H14+1}) : {distance(positions[O1], positions[H14]):.3f} Å")
    print(f"  O2({O2+1}) - C8({C8+1}) : {distance(positions[O2], positions[C8]):.3f} Å")
    print(f"  O2({O2+1}) - H9({H9+1}) : {distance(positions[O2], positions[H9]):.3f} Å")

    # Bond angles
    print("\n🔹 Bond Angles (°)")
    print(f"  C13({C13+1}) - O1({O1+1}) - H14({H14+1}) : {angle(positions[C13], positions[O1], positions[H14]):.2f}°")
    print(f"  C8({C8+1}) - O2({O2+1}) - H9({H9+1}) : {angle(positions[C8], positions[O2], positions[H9]):.2f}°")

    # dihedral angles
    print("\n🔹 Dihedral Angles (°) (If applicable)")
    if len(atoms) >= 4:  # Ensure enough atoms exist
        print(f"  C13({C13+1}) - O1({O1+1}) - O2({O2+1}) - C8({C8+1}) : {dihedral(positions[C13], positions[O1], positions[O2], positions[C8]):.2f}°")

    print("=" * 50)

if __name__ == "__main__":
    main()

import os
import subprocess

# Define the input and output folders
ligands_folder = 'E:/ABC/ligands' 
output_folder = 'E:/ABC/pdbqt'

# Iterate through the ligands folder
for filename in os.listdir(ligands_folder):
    # Check if the file is a ligand file
    if filename.endswith('.pdb'):
        # Create the input and output file paths
        ligand_file = os.path.join(ligands_folder, filename)
        output_file = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.pdbqt')

        # Execute Open Babel command to convert the ligand file
        subprocess.call(['obabel', ligand_file, '-o', 'pdbqt', '-O', output_file])

        print(f"Converted {filename} to {output_file}")

print("Conversion complete!")

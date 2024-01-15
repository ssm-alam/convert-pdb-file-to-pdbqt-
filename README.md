# convert-pdb-file-to-pdbqt-
# Ligand PDB to PDBQT Converter

This Python script enables the conversion of multiple ligand files in PDB format to PDBQT format simultaneously using Open Babel.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/ssm-alam/convert-pdb-file-to-pdbqt-.git
    cd pdb-to-pdbqt-converter
    ```

2. **Install Open Babel:**
   - Install Open Babel using pip:
      ```bash
      pip install openbabel
      ```
    -  Alternatively, follow the instructions on (https://open-babel.readthedocs.io/en/latest/index.html) to install Open Babel on your system.

4. **Set Up Virtual Environment (Optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

5. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Converter:**
    ```bash
    python convert_pdb_to_pdbqt.py
    ```

7. **Input and Output Folders:**
    - Modify the `ligands_folder` and `output_folder` variables in the script to point to your input and output directories.

8. **Convert Multiple Ligands:**
    - The script iterates through all PDB files in the specified input folder and converts each to PDBQT format.

9. **Conversion Output:**
    - The converted PDBQT files will be created in the specified output folder.

## Requirements

- Python 3.x
- Open Babel

## License

NONE

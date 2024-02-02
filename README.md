_Authors_: Jade COCHET, Naëla GOURRI

# Creation of an objective function for the RNA folding problem

For a given ribonucleotide chain, the RNA folding problem involves finding the native fold
among the astronomically large number of possible conformations. The native fold being the
one with the lowest Gibbs free energy, the objective function should be an estimator of this
energy. Meaning that we'll estimate the most probable RNA conformation.

## Usage:
To execute the project and apply it to a PDB file of your choosing, follow this: 
- Ensure you have Python installed on your system.
- Open a terminal and navigate to the project directory.
- Execute the following command, replacing `file.pdb` with the path to your PDB file:
 ```bash
   python main.py file.pdb
  ```

The outputs will be saved in the output_directory.


## Project Description:
We have two Python scripts :
- training.py: contains all the functions for retrieving  

- main.py: 

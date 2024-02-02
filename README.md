_Authors_: Jade COCHET, Naëla GOURRI

# Creation of an objective function for the RNA folding problem

For a given ribonucleotide chain, the RNA folding problem involves finding the native fold
among the astronomically large number of possible conformations. The native fold being the
one with the lowest Gibbs free energy, the objective function should be an estimator of this
energy. Meaning that we'll estimate the most probable RNA conformation.

## Usage:
To execute the project and apply it to a PDB file of your choosing, follow this: 
- Ensure you have Python and R installed on your system.
- Open a terminal and navigate to the project directory.
- Execute the following command, replacing `file.pdb` with the path to your PDB file:
 ```bash
   python main.py file.pdb
 ```

The outputs will be saved in the output_directory.


## Project Description:
### Scripts
**We have two Python scripts**

The file `training.py` contains all the functions to:
   - retrieve the bases (_C3_ & _'ATOM'_, as only _C3_ atoms are taken into account);
   - compute interatomic distances from the given dataset of PDB files;
   - compute the observed frequencies: 10 × 20 distance intervals (0 to 20 Å);
   - compute the reference frequency (= the “XX" pair);
   - compute the scores(pseudo-energy) of the two frequencies;
   - compute the estimated Gibbs free energy of the evaluated RNA conformation.
  
The file `main.py` executes all previous functions and outputs 10 files for the frequencies of the 20 distances and Gibbs free energy. It also calls the R file for the plotting.


**We also have a R script**

The file `plot.r` plots the interaction profiles, the score as a
function of the distance.

### Example
We computed the project for an example file `example_pdb/17ra.pdb`. 

The scores calculated can be found in the `example_scores` directory with the file as follows: _`pair.txt`_ (i.e. _`AA.txt`_, ..., _`CG.txt`_, ..., _`UU.txt`_).

The corresponding plots to each of those can be found in the `example_plot` directory with the file as follows: _`interaction_profile_pair.png`_.

The estimated Gibbs free energy of the evaluated RNA conformation can be found in the `example_result` directory with the file _`gibbs_free_energy.txt`_. This file contains the estimation for every conformation (for example _**line 1 =** "AA: 140.504"_) but it also returns the minimum value among those and predict the native fold, here: _**line 11 =** "The most probable native fold structure conformation is CG"_.


### RNA PUZZLES
The 29 RNA PDB files from the RNA PUZZLES data (Cruz et al. (2012)) can also be found in its namesake directory. 

###### Cruz, José, Marc-Frédérick Blanchet, Michal Boniecki, Janusz Bujnicki, Shi-Jie Chen, Song Cao, Rhiju Das, et al. 2012. “RNA-Puzzles: A CASP-like evaluation of RNA three-dimensional structure prediction.” RNA (New York, N.Y.) 18 (February): 610–25. https://doi.org/10.1261/rna.031054.111.






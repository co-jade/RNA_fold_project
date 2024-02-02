import os
import sys
import subprocess
from training import *

# open the file in input
if len(sys.argv) != 2:
    print("Wrong number of arguments")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file) as file:
    retrieve_bases(file)

# Generate pair lists for each combination of bases
pair_lists = {}

pair_lists["AA"] = generate_pair_list(list_A, list_A)
pair_lists["AU"] = generate_pair_list(list_A, list_U)
pair_lists["AC"] = generate_pair_list(list_A, list_C)
pair_lists["AG"] = generate_pair_list(list_A, list_G)
pair_lists["UU"] = generate_pair_list(list_U, list_U)
pair_lists["UC"] = generate_pair_list(list_U, list_C)
pair_lists["UG"] = generate_pair_list(list_U, list_G)
pair_lists["CC"] = generate_pair_list(list_C, list_C)
pair_lists["CG"] = generate_pair_list(list_C, list_G)
pair_lists["GG"] = generate_pair_list(list_G, list_G)

# compute observed frequencies:
frequencies = compute_obs_frequencies(pair_lists)

# compute reference frequency
ref_freq = compute_ref_frequency(pair_lists)

# compute scores
scores = compute_scores(frequencies, ref_freq)

# output the 10 files for the frequencies of the 20 distances 
output_directory = "scores"
os.makedirs(output_directory, exist_ok=True)

for base_pair, distance in scores.items():
    file_path = os.path.join(output_directory, f"{base_pair}.txt")
    with open(file_path, 'w') as file:
        for score in distance.values():
            file.write(f"{score}\n")

# appelle de la fonction r pour les plots
score_files = os.listdir("scores")

for file in score_files:
    r_script_path = 'plot.r'
    r_command = f'Rscript "{r_script_path}" "{os.path.join("scores", file)}"'
    subprocess.run(r_command, shell=True)


# computing Gibbs free energy
gibbs_free_energies = compute_GFE(scores)

# output Gibbs free energy
out_file = f"gibbs_free_energy.txt"
with open(out_file, 'w') as file:
    for base_pair, gfe in gibbs_free_energies.items():
        file.write(f"{base_pair}: {gfe}\n")
    min_gfe = min(gibbs_free_energies, key = gibbs_free_energies.get)
    file.write(f"The most probable native fold structure conformation is {min_gfe}")
        





import os
import sys
import math

#c = 0
list_A = []
list_U = []
list_C = []
list_G = []

def retrieve_bases(file):
    for line in file :
        if "ATOM" in line and "C3'" in line :
            l = line.split()
            if l[3] == "A" :
                list_A.append([l[3],l[4],l[5],l[6],l[7],l[8]])#base, chain identifier, residue sequence number, x, y, z
            if l[3] == "U" :
                list_U.append([l[3],l[4],l[5],l[6],l[7],l[8]])
            if l[3] == "C" :
                list_C.append([l[3],l[4],l[5],l[6],l[7],l[8]])
            if l[3] == "G" :
                list_G.append([l[3],l[4],l[5],l[6],l[7],l[8]])
            #print(liste_bases[-1])
            #c +=1
            # !!! no retrun ? !!! Soit faire en sorte que la fonction fasse une seule base à la fois soit réussir à retourner les 4 listes 

def generate_pair_list(base1, base2):
    pair_list = []
    for i in base1:
        for j in base2:
            if i[1] == j[1] and abs(int(i[2]) - int(j[2])) > 3:
                if i[0]==j[0] :
                    if i<j:
                        xi, xj = float(i[3]), float(j[3])
                        yi, yj = float(i[4]), float(j[4])
                        zi, zj = float(i[5]), float(j[5])
                        pair_list.append(round(((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)**0.5, 3))
                else :
                   xi, xj = float(i[3]), float(j[3])
                   yi, yj = float(i[4]), float(j[4])
                   zi, zj = float(i[5]), float(j[5])
                   pair_list.append(round(((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)**0.5, 3)) 
    if pair_list != [] : return pair_list
    else: return[0]

def compute_obs_frequencies(pair_lists):
    frequencies = {}
    for base_pair in pair_lists.items():
        distances = {}
        for i in range (0, 20): #initialisation of dictionnary 
            distances[i] = 0
        for obs in base_pair[1]: #count of the distances
            if obs < 20:
                distances[int(obs)] = distances[int(obs)] + 1
        for i in range (0, 20): #calculating the frequency (percentage) of observed frequencies
            distances[i] = round((distances[i] / len(base_pair[1])*100), 2)
        frequencies[base_pair[0]] = distances
    return frequencies

def compute_ref_frequency(pair_lists):
    ref_freq = {}
    for i in range (0,20): #initialisation of distionnary
        ref_freq[i] = 0
    total = 0
    for base_pair in pair_lists.items():
        total = total + len(base_pair[1])
        for obs in base_pair[1]:
            if obs < 20:
                ref_freq[int(obs)] = ref_freq[int(obs)] + 1
    for i in range(0,20):
        ref_freq[i] = round((ref_freq[i]/total)*100, 2)   
    return ref_freq

def compute_scores(frequencies, ref_freq):
    scores ={}
    for base_pair in frequencies.items():
        distances = {}
        for i in range (0, 20): #initialisation of dictionnary 
            if ref_freq[i] == 0:
                distances[i] = 10 #minimum instead of -inf
            elif base_pair[1][i] == 0:
                distances[i] = 10 #maximum instead of +inf
            else :
                distances[i] = round(-math.log(base_pair[1][i]/ref_freq[i]), 3)
        scores[base_pair[0]] = distances
    return scores

def compute_GFE(scores):
    gibbs_free_energies = {}
    for base_pair, distance in scores.items():
        gibbs_free_energy = 0
        for score in distance.values():
            gibbs_free_energy = round(gibbs_free_energy + score, 3)
        gibbs_free_energies[base_pair] = gibbs_free_energy    
    return gibbs_free_energies

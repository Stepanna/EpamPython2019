# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:26:18 2019

@author: nyna
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string

# read the file dna.fasta
fasta = open('dna.fasta', 'r')
count_file = open('count_nucleotides.txt', 'w', encoding='UTF-8')
rna_file = open('translate_to_rna.txt', 'w', encoding='UTF-8')
codon_seq = open('codon_seq.txt', 'w', encoding='UTF-8')

rna_codon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
             "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
             "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
             "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
             "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
             "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
             "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
             "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
             "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
             "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
             "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
             "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
             "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
             "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
             "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G",
             "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
             }

header, parts_of_seq, dna, sequence = [], [], {}, ''
for line in fasta:
    if line[0]=='>':
        if parts_of_seq:
            sequence = sequence.join(parts_of_seq)
            dna.update({header: sequence})
        header = line[1:-1]
        parts_of_seq = []
        sequence = ''
    else:    
        parts_of_seq.append(line[0:-1])
sequence = sequence.join(parts_of_seq)
dna.update({header: sequence})

def count_nucleotides(dna):
    #Построение статистики по входящим в последовательность ДНК нуклеотидам 
    #для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])
    num_of_nucleotides = {}
    #nucl_dataFrame = pd.DataFrame()
    for c in ('ACGT'):
        num_of_nucleotides.update({c: value.count(c)})
        nucl_dataFrame = pd.DataFrame.from_records(num_of_nucleotides, index = [0])
    count_file.write(f'Статистика для {key}:\n')
    #count_file.write(f'{num_of_nucleotides.items()}')
    
    for k, v in num_of_nucleotides.items():
        count_file.write(str(k) + ' - '+ str(v) + '\n')
    
    nucl_dataFrame.plot.bar(title=key)
    name = key.replace(" ", "") + '.png'
    plt.savefig(name)
    return num_of_nucleotides

def translate_from_dna_to_rna(dna):
    #Перевод последовательности ДНК в РНК
    rna, nucleotides = '', []
    for i,j in enumerate(value):
        if j == 'T':
            nucleotides.append('U')
        else:
            nucleotides.append(j)
    rna = rna.join(nucleotides)
    rna_file.write(f'{key}: {rna}\n')
    return rna

def translate_rna_to_protein(rna):
    #Перевод последовательности РНК в протеин
    protein = ''
    for i in range(0, (len(rna)-(1+len(rna)%3)), 3):
        if rna_codon[rna[i:i+3]] == "Stop" :
            break
        protein += rna_codon[rna[i:i+3]]
    codon_seq.write(f'Последовательность кодонов для {key}: {protein}\n')    
    return protein

for key, value in dna.items():
    count_nucleotides(dna)
    rna = translate_from_dna_to_rna(dna)
    translate_rna_to_protein(rna)
    
count_file.close()
rna_file.close()
fasta.close()
codon_seq.close()
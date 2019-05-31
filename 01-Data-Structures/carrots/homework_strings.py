import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string

#parse rna_codon_table to dict rna_codon
txtline, rna_codon = [], {}
rna_codon_table = open('rna_codon_table.txt', 'r')
for line in rna_codon_table:
    txtline.extend(line.split())
for i, j in enumerate(txtline):
    for k in range(0, len(txtline), 2):
        rna_codon.update({txtline[k]: txtline[k+1]})
rna_codon_table.close()

# read the file dna.fasta
fasta = open('dna.fasta', 'r')
header, parts_of_seq, dna_dict, sequence = [], [], {}, ''
for line in fasta:
    if line[0]=='>':
        if parts_of_seq:
            sequence = sequence.join(parts_of_seq)
            dna_dict.update({header: sequence})
        header = line[1:-1]
        parts_of_seq = []
        sequence = ''
    else:    
        parts_of_seq.append(line[0:-1])
sequence = sequence.join(parts_of_seq)
dna_dict.update({header: sequence})
fasta.close()

def count_nucleotides(dna_dict):
    #Построение статистики по входящим в последовательность ДНК нуклеотидам 
    #для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])
    count_file = open('count_nucleotides.txt', 'w', encoding='UTF-8')
    for key, value in dna_dict.items():
        num_of_nucleotides = {}
        for c in ('ACGT'):
            num_of_nucleotides.update({c: value.count(c)})
            nucl_dataFrame = pd.DataFrame.from_records(num_of_nucleotides, index = [0])
        count_file.write(f'Статистика для {key}:\n')
        
        for k, v in num_of_nucleotides.items():
            count_file.write(str(k) + ' - '+ str(v) + '\n')
        
        nucl_dataFrame.plot.bar(title=key)
        name = key.replace(" ", "") + '.png'
        plt.savefig(name)
    count_file.close()

def translate_from_dna_to_rna(dna_dict):
    #Перевод последовательности ДНК в РНК
    rna_file = open('translate_to_rna.txt', 'w', encoding='UTF-8')
    rna_dict = {}
    for key, value in dna_dict.items():
        rna, nucleotides = '', []
        nucleotides = ['U' if value[i] == 'T' else j for i, j in enumerate(value)]
        rna = rna.join(nucleotides)
        rna_dict.update({key: rna})
        rna_file.write(f'{key}: {rna}\n')
    rna_file.close()    
    return rna_dict

def translate_rna_to_protein(rna_dict):
    #Перевод последовательности РНК в протеин
    codon_seq = open('codon_seq.txt', 'w', encoding='UTF-8')
    for key, value in rna_dict.items():
        protein = ''
        for i in range(0, (len(value)-(1+len(value)%3)), 3):
            if rna_codon[value[i:i+3]] == "Stop" :
                break
            protein += rna_codon[value[i:i+3]]
        codon_seq.write(f'Последовательность кодонов для {key}: {protein}\n') 
    codon_seq.close()

count_nucleotides(dna_dict)
rna_dict = translate_from_dna_to_rna(dna_dict)
translate_rna_to_protein(rna_dict)
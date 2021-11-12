import sys
import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='This converts sequence_IDs from a gff3 to sequence_IDs from a given genome fasta file')
parser.add_argument("--genome", help="This is the genome fasta")
parser.add_argument("--gff3", help="This is the gff3 file")
parser.add_argument("--prefix", help="This is the prefix for the output file")

args = parser.parse_args()
NCBI_genome = args.genome
Gff3_file = args.gff3
prefix = args.prefix

new_file = str(prefix) + "_renamed.gff3"

with open(NCBI_genome, 'r') as genome:
    NCBI_2_ChrID = {}
    NCBI_list = []
    for line in genome:
        if  line.startswith(">"):
            cols = line.rstrip("\n").split(" ") # get columns
            NCBI_ID = cols[0].split('>')[1]
            Chr_ID = cols[6]
            NCBI_2_ChrID[Chr_ID] = NCBI_ID
            NCBI_list.append(NCBI_ID)
# %%
for i in NCBI_2_ChrID:
    print(i, '-->', NCBI_2_ChrID[i])

# %%    
with open(new_file, 'w') as new_file:
    with open(Gff3_file, 'r') as gff3:
        for line in gff3:
            if not line.startswith("#"): # ignore first few lines
                cols = line.rstrip("\n").split("\t") # get columns
                chr = cols[0]
                if chr in NCBI_list:
                    line = "\t".join(cols)
                    new_file.write(line + '\n')
                else:
                    match = NCBI_2_ChrID[chr]
                    cols[0] = match
                    line = "\t".join(cols)
                    new_file.write(line + '\n')
        else:
            new_file.write(line + '\n')

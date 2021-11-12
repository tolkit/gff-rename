# gff-rename

Replace the sequence IDs in a gff3 file with a set of provided sequence IDs from a genom.fasta.
This is useful when a gff3 file is retrieved from Ensembl whereas the genome.fasta is from NCBI as the gff3 file will use Chromosome IDs whereas the genome.fasta will use GenBank sequence IDs. Running this script will convert the sequence IDs in the gff3 file to match those from the genome.

## Install
```

git clone https://github.com/tolkit/gff-rename
cd gff-rename
chmod +x gff-rename
```

## Usage

`gff-rename`

```
gff3-rename
Charlotte Wright <cw22@sanger.ac.uk> 
Convert_gff3_IDs.py [-h] [--genome GENOME] [--gff3 GFF3] [--prefix PREFIX]

This converts sequence_IDs from a gff3 to sequence_IDs from a given genome fasta file

optional arguments:
  -h, --help       show this help message and exit
  --genome GENOME  This is the genome fasta
  --gff3 GFF3      This is the gff3 file
  --prefix PREFIX  This is the prefix for the output file
  ```

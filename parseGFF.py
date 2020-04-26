#! /usr/bin/env python3

# import module
import argparse 
import csv
import re
from Bio import SeqIO
from collections import defaultdict

def get_args():
    # argument parser object
    parser = argparse.ArgumentParser(description = "This script parses a GFF file")

    # add positional argument for the input position in the GFF file
    parser.add_argument("gff", help="name of the GFF file")
    parser.add_argument("fasta", help="name of the FASTA file")

    # parse the arguments 
    return parser.parse_args()

def parse_fasta():
    # read and parse the FASTA file
    return SeqIO.read(args.fasta, "fasta")

def parse_gff(genome):
    # read the GFF file 
    with open(args.gff, "r") as gff_file:
        # csv reader object
        reader = csv.reader(gff_file, delimiter="\t")
        for line in reader:
            if not line:
                continue
    
            else:
                organism = line[0].replace(" ", "_")
                feature_type = line[2]
                start = int(line[3])
                end = int(line[4])
                strand = line[6]
                attributes = line [8]
            # extract this feature from the genome
                if feature_type == "CDS":
                    feature_seq = genome[start-1:end]
                    if strand == "-":
                        reverse_complement = feature_seq[::-1]
                        print(reverse_complement)
                    # extract the gene name
                    match = re.search("Gene\s+(\S+)\s+", attributes)
                    gene_name = match.group(1)
                    # extract the exon number
                    exon = re.search("exon\s+(\d+)\s+", attributes)
                    exon_number = exon.group(1)
                    # dictionary called cds where, key = gene name, value = another dictionary (key = exon number, value = sequence of that exon)
                    # declare the dictionary, key = exon number and value = sequence of that exon
                    exon_dict = defaultdict(dict)
                    exon_dict={
                        "exon_number" : "feature_seq" # key is exon number and value is exon sequence 
                        }
                    cds={
                        "gene_name" : "exon_dict" # key is gene name and value is another dictionary
                        }
                    # print FASTA format
                    print(">" + organism + "_" + gene_name)
                    #print(feature_seq)
                    #print(attributes)
                    #print(feature_seq)
                    #feature_GC = gc(feature_seq.seq)
                    #GCround = round(feature_GC, 2)
                    #print (GCround)
           
def gc(sequence):
    # calculate and print the GC content for that substring (2 decimal places) 
    count_of_G = sequence.count("G")
    count_of_C = sequence.count("C")
    return (count_of_G + count_of_C/len(sequence)


def codon2aa(codon):
    codon_dict = {'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAA':'O', 'TAC':'Y', 'TAG':'O', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TGA':'O', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'}

    return(codon_dict.get(codon, "-"))

def main():
    genome_sequence = parse_fasta()
    parse_gff(genome_sequence.seq)


# get the command-line argumetns before calling main()
args = get_args()

# execute the program by calling main
if __name__ == "__main__":
    main()



                  



            

            
            
                
            
        

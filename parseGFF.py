#! /usr/bin/env python3

# import module
import argparse 
import csv
from Bio import SeqIO
 
# create an argument parser object
parser = argparse.ArgumentParser(description = "This script parses a GFF file")

# add positional argument for the input position in the GFF file
parser.add_argument("gff", help="the name of the GFF file")
parser.add_argument("fasta", help="name of the FASTA file")

# parse the arguments 
args = parser.parse_args()

# read and parse the fasta file
genome = SeqIO.read(args.fasta, "fasta")

# read GFF file
with open(args.gff, "r") as gff_file:
    reader = csv.reader(gff_file, delimiter="\t")
    for line in reader:
        if not line:
            continue
        else:
            # test whether this is a CDS feature
            feature = line[2]
            if feature != "CDS":
                continue
            else:
                start = line[3]
                end = line[4]
                print(start,end)
                                                   
                
                
        
# extract the CDS sequence 
                with open(args.fasta, "r") as fasta:
                    print()

            # if it is a CDS feature, then extract the substring/sequence
            dna = open(args.fasta, "r")
            length = len(str(dna))
            
            # calculate and print the GC content for substring to 2 decimal places

            # calculate the number of each base 
            c_count = dna.count("C")
            g_count = dna.count("G")
            # calculate the base composiiton
            gc_content = (c_count + g_count / length)
            gc_round = round(gc_content, 2) 
            print(gc_round +"\n") 
                
# store each line as a list
list=[]


            
        

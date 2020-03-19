#! /usr/bin/env python3

# define the input file
infile = "/Users/savannahwashburn/Desktop/watermelon_files/watermelon.gff"

# create list
mylist = []

# open the file 
with open(infile, "r") as watermelon:
    for list in watermelon:
        mylist.append(list)
        gene = list.rstrip("\n")
        name = gene.split(",")
# extract the genes
        if(name[7] == "Gene"):
            print.sort(",".join([name[7], name[8]]))

infile.close()



            
        

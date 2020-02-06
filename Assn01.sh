#Washburn assn01-1#

#! /bin/bash
find . -name \nad* -print

#Washburn assn01-2#

#! /bin/bash
top

#12.20% of my CPU is being used by the top command.#
#MemRegions: 124560 total, 3132M resident, 93M private, 679M shared. PhysMem: 7910M used (1796M wired), 281M unused.#
#These numbers were derived from this command (copy and pasted from command).#

#Washburn assn01-3#

#! /bin/bash
cd /Users/savannahwashburn/Desktop/Programming_for_Biologists/watermelon_files 
grep 'misc_feature' watermelon.gff > IR_regions.gff
sort -k7gr IR_regions.gff


#Washburn assn01-4#

#! /bin/bash
cd /Users/savannahwashburn/Desktop/Programming_for_Biologists/watermelon_files
grep -c 'misc_feature' watermelon.gff
grep -cv 'misc_feature' watermelon.gff
grep 'misc_feature' watermelon.gff
grep -v 'misc_feature' watermelon.gff

#The number of fragments from the chloroplast's large IR region will outnumber the sequences from outside the IR. More chloroplast fragment come from inside the IR.#


#Washburn assn01-5#

#! /bin/bash
cd /Users/savannahwashburn/Desktop/Programming_for_Biologists/watermelon_files/watermelon_nt
grep 'GGATCC' *.fasta > BamHI
grep -v 'GAATTC' BamHI > BamHI_lack_EcoR1
less -SN BamHI_lack_EcoR1

#There are watermelon genes that contin the BamHI region but lack the EcoRI region.#


#Washburn assn01-06#

#! /bin/bash
cd /Users/savannahwashburn/Desktop/Programming_for_Biologists/example_files 
cat shaver_etal.csv | head -n 1000 | tail -n 500


#Washburn assn01-7#

#! /bin/bash
cd /Users/savannahwashburn/Desktop/Programming_for_Biologists/example_files
sort -k2,2r -k3,3 fruit.txt

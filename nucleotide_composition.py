#! /bin/bash 

# read dna.txt
input_file = "dna.txt"
print(input_file)

infile = open("dna.txt", "r")

file_contents = infile.read()
# close the file
my_file.close()

# calculate number of each base
my_dna = open("dna.txt")
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
c_count = my_dna.count('C')
g_count = my_dna.count('G')

# calculate base composition
length = len(my_dna)
a_content = a_count / length
t_content = t_count / length
c_content = c_count / length
g_content = g_content / length

# round each decimal
a_round = round(a_content, 2)
t_round = round(t_content, 2)
c_round = round(c_content, 2)
g_round = round(g_content, 2)

# print the contents of sequence
print("the file contents are " + "\n" "A: " + str(a_round) + "\n" + "T: " str(t_round) + "\n" + "C: " + str(c_round) + "\n" + "G: " + str(g_round) + "\n")   

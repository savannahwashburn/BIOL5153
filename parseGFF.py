#! /usr/bin/env python3

# define the file
file = "/Users/savannahwashburn/Desktop/watermelon_files/watermelon.gff"

# create list
mylist = []

# open the file 
with open(file, "rt") as watermelon:
    for list in watermelon:
        name = list.split()[10]
        # name from line
        if not name == "similar":
            #ignore similar
            mylist.append(name)

#sort list
mylist.sort()
#print list 
print(mylist) 






            
        

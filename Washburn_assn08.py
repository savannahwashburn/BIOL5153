#! /usr/bin/env python3

# import modules 
import re
from prettytable import PrettyTable

# define the variable 
concert = str("Katherine went to the concert to see Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out.")

# for loop to determine the variations of the name

for match in re.finditer("[K|C]ath[a-z]+", concert, re.I):
    start = match.start()
    end = match.end()
    # print the output in a table
    x = PrettyTable()
    x.field_names = ["The Full Match", "Position of First Character in the Match", "Position of Last Character in the Match", "Length of Match"]
    x.add_row([match.group(0), str(start), str(end), end-start])
    print(x)


   


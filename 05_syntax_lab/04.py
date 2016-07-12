from random import randint
from array import array

"""
Recive lines until getting empty one and printing them beckword
"""

lines = []
line = raw_input()
lines.insert(0, line)

while line != '': 
        line = raw_input()
        lines.insert(0, line)
        

for l in lines:
        print  l
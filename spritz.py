import numpy as np

# Open text file
results = []
with open('spritz.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))



print (results)

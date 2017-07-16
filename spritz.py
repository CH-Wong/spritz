import numpy as np

# Open text file
results = []
with open('spritz.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

print("HALLO DIT HEB IK NET VERANDERD OP VINCENTS PC!")

print("HALLO DIT HEB IK NET VERANDERD OP MIJN EIGEN PC")

print("OHJA, VINCENT IS DIK.")

print("MERGE FOUT 1")

print (results)

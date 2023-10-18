#!/usr/bin/env python3

import sys

dna = sys.argv[1].upper()

print(dna.count('A'), 'adenines', end = ' ') 
print(dna.count('T'), 'thymines', end = ' ') 
print(dna.count('C'), 'cytocines', end = ' ') 
print(dna.count('G'), 'guanines') 

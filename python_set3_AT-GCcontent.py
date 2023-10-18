#!/usr/bin/env python3

import sys

dna = sys.argv[1].upper()

AT = (dna.count('T')+dna.count('A'))/len(dna) 
GC = (dna.count('G')+dna.count('C'))/len(dna)

print(f'AT-content: {AT:.2f}', end='')
print(f' GC-content: {GC:.2f}')



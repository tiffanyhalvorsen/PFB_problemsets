#!/usr/bin/env python3

import sys

seq = sys.argv[1].upper()

# create set of unique nucleotides in sequence
nt_comp = set(seq)
print(f'Unique nucleotides in sequence: {nt_comp}')

# create an empty dict for nt counts
nt_count = {}

# count total number of nt's in input seq
for nt in nt_comp:
	count = seq.count(nt)
	nt_count[nt] = count

# determine GC content
GC = (seq.count('G')+seq.count('C'))/len(seq)

print(f'Total count of each nt: {nt_count}')
print(f'GC-content: {GC:.2f}')

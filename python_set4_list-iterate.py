#!/usr/bin/env python3

import sys

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seqs:
	print(seqs.index(seq), len(seq), seq, sep = '\t') 

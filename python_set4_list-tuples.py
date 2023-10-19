#!/usr/bin/env python3

import sys


seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

pairs = [(len(seq), seq) for seq in seqs]
print(pairs)

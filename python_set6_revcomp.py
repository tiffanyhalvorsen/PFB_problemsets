#!/usr/bin/env python3

gene_dict = {}
with open("./Python_06.seq.txt") as seq_file:
	for line in seq_file:
		line = line.rstrip()
		seq_name,seq = line.split()
		rev_comp = seq[::-1]
		print(f'{seq_name}\t{seq}\tReverse complement')


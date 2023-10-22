#!/usr/bin/env python3

import sys
import re

input_file = sys.argv[1]

fastaDict = {}
with open(input_file, "r") as fasta_all:
	for line in fasta_all:
		line = line.rstrip()
		if line.startswith('>'):
			match = re.search(r'^>(\S+)\s+(.+)$', line)
			seq_id = match.group(1)
			desc = match.group(2)
			fastaDict[seq_id] = {'desc':desc,
													 'seq':""}
		else:
			fastaDict[seq_id]['seq'] += line
		
print(fastaDict)

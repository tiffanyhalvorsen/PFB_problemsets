#!/usr/bin/env python3

import sys
import re

input_file = sys.argv[1]

fastaDict = {}
with open(input_file, "r") as fasta_all:
	for line in fasta_all:
		line = line.rstrip()
		if line.startswith('>'):
			match = re.search(r"^>(\S+)", line)
			seq_id = match.group(1)
			fastaDict[seq_id] = ""
		else:
			fastaDict[seq_id] += line
		
print(fastaDict)

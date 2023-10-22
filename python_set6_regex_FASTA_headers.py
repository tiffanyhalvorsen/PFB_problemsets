#!/usr/bin/env python3

import sys
import re

fasta_file = sys.argv[1]

lines = ""
with open(fasta_file, "r") as file:
	for line in file:
		for match in re.finditer(r'^>(\S+)\s+(.+)$', line):
			print(f'id: {match.group(1)}\tdesc: {match.group(2)}')

		


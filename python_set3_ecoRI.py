#!/usr/bin/env python3

import sys

dna = sys.argv[1].upper()
re_site = sys.argv[2].upper()

if re_site in dna:
	print(f'EcoRI site found at nt position: {dna.find(re_site)+1} to {dna.find(re_site)+len(re_site)+1}')
elif re_site[::-1] in dna:
	print(f'EcoRI reverse complement site found at nt position: {dna.find(re_site[::-1])+1} to {dna.find(re_site)+len(re_site)+1}')
else:
	print('No EcoRI restriction site found')

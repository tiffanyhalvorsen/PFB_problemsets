#!/usr/bin/env python3

import sys
import re

fasta_file = sys.argv[1]

# start with fasta parser, create dictionary of seq_id keys and a dictionary of values that starts with the rest of the fasta header (desc) and the raw sequence from the fasta record.

fastaDict = {}
with open(fasta_file, "r") as file:
	for line in file:
		line = line.rstrip()
		if line.startswith('>'):
			match = re.search(r'^>(\S+)\s+(.+)$', line)
			seq_id = match.group(1)
			desc = match.group(2)
			fastaDict[seq_id] = {'desc':desc,
                             'seq':'',
                             'frame1':'',
														 'frame2':'',
														 'frame3':''}
														
		else:
			fastaDict[seq_id]['seq'] += line

# now, include a record for each seq_id in the nested dictionary that includes the first open reading frame from each raw sequence with spaces between codons.

for seq_id in fastaDict:
	for sequence in fastaDict[seq_id]:
		seq = fastaDict[seq_id]['seq']
		#match = re.search(r"ATG\w+TA[AG]", seq)
		# find all sequences that start with ATG, have intervening sequence, and end with TAA/TAG
		matches = re.finditer(r"(ATG\w+TA[AG])",seq)
		if match:
			for match in matches:
				# filter on sequences that are divisible by 3 and longer than 40 nt
				if (len(match.group()) % 3 == 0) and (len(match.group())) > 40:
					# find frame
					upstream = len(match.group()) - int(match.start())
					codons = []
					start = match.start()
					end = match.end()
					orf = seq[start:end]
					if upstream % 3 == 0:
						fastaDict[seq_id]['frame1'] = match.group()
						for nts in range(0,len(match.group()), 3):
							print(type(match.group()))
# Fix issue with splitting sequences into codons. Then double check sequence output.
							#codons.append(match.group()[nts:nts+3])
							#codons = ' '.join(codons)
						print(codons)
					elif (upstream+1) % 3 == 0:
						fastaDict[seq_id]['frame1'] = 'No ORF'
						fastaDict[seq_id]['frame2'] = match.group()
					elif (upstream+2) % 3 == 0:
						fastaDict[seq_id]['frame1'] = 'No ORF'
						fastaDict[seq_id]['frame2'] = 'No ORF'
						fastaDict[seq_id]['frame3'] = match.group()
						#print(fastaDict[seq_id]['frame1'])
						#print(fastaDict[seq_id]['frame2'])
						#print(fastaDict[seq_id]['frame3'])
					# Add some code to split ORFs into reading frames.
					# Check that loop iterates through FASTA records
					
					#if len(match.groups()) == 1:
					#	codons1 = []
					#	start1 = match.start(1)
					#	end1 = match.end(1)
					#	orf1 = seq[start1:end1]
					#	for nts in range(0,len(orf1), 3):
					#		codons1.append(orf[nts:nts+3])
							#print(codons)
					#		orf_frame1 = ' '.join(codons1)
		else:
			orf_frame1 = 'No ORF'
			orf_frame2 = 'No ORF'
			orf_frame3 = 'No ORF'
		#fastaDict[seq_id]['frame1'] = orf1
		#for key, value in fastaDict.items():
		#	seq_ID = key
		#print(f'{seq_id}-frame-1-codons\n{orf1}')




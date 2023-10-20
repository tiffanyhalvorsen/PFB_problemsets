#!/usr/bin/env python3

nlines = 0
nchars = []
with open("Python_06.fastq", "r") as seq_file:
	for line in seq_file:
		line = line.rstrip()
		nchars.append(len(line))
		nlines += 1

print(f'Total # of lines: {nlines}. Total # of characters: {sum(nchars):d}. Average line length: {sum(nchars)/nlines:f}')  

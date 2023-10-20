#!/usr/bin/env python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as file_read, open(output_file, "w") as file_write:
	for line in file_read:
		line = line.rstrip()
		line = line.upper()
		file_write.write(line)

print('Wrote new file with uppercase lines.') 

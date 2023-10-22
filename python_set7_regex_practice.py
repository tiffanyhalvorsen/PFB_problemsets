#!/usr/bin/env python3

import sys
import re

file = sys.argv[1]

text = ""
with open(file) as x:
	for line in x:
		#line = line.rstrip()
		text += line

for match in re.finditer(r"Nobody", text):
	print(f'{match.group()}\t{match.start()}\t{match.end()}')

new_text = re.sub(r'Nobody', 'Eric', text)
output = open('eric.txt', 'w')
output.write(new_text)
output.close()
				

#!/usr/bin/env python3

import sys

genes_all = sys.argv[1]
genes_stemcell = sys.argv[2]
genes_pigment = sys.argv[3]
genes_regulators = sys.argv[4]

ids = set()
with open(genes_all, "r") as file:
	for line in file:
		line = line.rstrip()
		ids.add(line)

ids_stemcell = set()
with open(genes_stemcell, "r") as file:
	for line in file:
		line = line.rstrip()
		ids_stemcell.add(line)

ids_pigment = set()
with open(genes_stemcell, "r") as file:
	for line in file:
		line = line.rstrip()
		ids_pigment.add(line)

ids_regulators = set()
with open(genes_regulators, "r") as file:
	for line in file:
		line = line.rstrip()
		ids_regulators.add(line)

stemcell_pigment_genes = ids_stemcell & ids_pigment
non_stemcell_genes = ids - ids_stemcell
stemcell_regulator_genes = ids_stemcell & ids_regulators

print(stemcell_regulator_genes)

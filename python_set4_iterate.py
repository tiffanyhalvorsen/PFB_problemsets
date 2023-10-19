#!/usr/bin/env python3

import sys

nums = [101,2,15,22,95,33,2,27,72,15,52]

even = 0
for num in nums:
	if num % 2 == 0:
		even += num
print(f'Sum of even numbers: {even}')

odd = 0
for num in nums:
	if num % 2 == 1:
		odd += num
print(f'Sum of odd numbers: {odd}')

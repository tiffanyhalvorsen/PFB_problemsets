#!/usr/bin/env python3

import sys

nums = list(range(1002))

num = 1000
factorial = 1000
while num >= 1:
	factorial = factorial * num
	num = num - 1
print(num, factorial)

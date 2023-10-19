#!/usr/bin/env python3

import sys

#for num in range(101):
#	print(num)

# nums = [num for num in range(101)]
# print(nums)

start = int(sys.argv[1])
end = int(sys.argv[2]) + 1

nums = [num for num in range(end)]

print(nums[start:end])

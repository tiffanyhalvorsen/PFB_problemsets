#!/usr/bin/env python3

import sys
num = int(sys.argv[1])

if num > 0:
  if num == 50:
    print("number is 50")
  elif num < 50:
    if num % 2 == 0:
      print("number is positive, <50, and even")
    elif num % 2 == 1:
      print("number is positive, <50, and odd")
  elif num > 50:
    if num % 2 == 0:
      print("number is positive, >50, and even")
    elif num % 2 == 1:
      print("number is positive, >50, and odd")
elif num < 0:
  print("number is negative")
else:
  print("numer is zero")




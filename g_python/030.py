#! /usr/bin/env python
import sys

seq = sys.argv[1]

for i in range(0, len(seq), 2):
   if seq[i:i+2] == "TT":
      print(seq[i:i+2]) 


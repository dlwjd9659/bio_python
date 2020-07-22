import sys

if len(sys.argv) != 2:
    print(

with open("059.fasta", 'r') as handle:
    for i in handle:
        
        print(i.count('A'))

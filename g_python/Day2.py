#25

Seq1 = 'ATGTTATAG'
for i in range(0, len(Seq1), 3):
    print(Seq1[i])
#print(Seq1[0], Seq1[3], Seq1[6])

######################
print("-------")

#26
Seq1 = 'ATGTTATAG'
for i in range(0, len(Seq1),3):
    #print(i, Seq1[i])
    print(i, i+3, Seq1[i:i+3])
    
#####################
print("-------")

#27
print(Seq1)
print(Seq1[::-1])

#####################
print("-------")

#28

d_seq = {"A":"T","T":"A","C":"G","G":"C"}
c_seq = ""
for i in Seq1:
    c_seq += d_seq[i]

print(Seq1)
print(c_seq)


#####################
#29
"C" in Seq1

#####################
print("------")
#30

seq = 'AGTTTATAG'

print(seq.find('T'))

print(seq[2:4])
print(seq[3:5])

print()

import sys

Seq1 = sys.argv[1]

for i in range(0, len(Seq1), 1):
    if Seq1[i:i+2] == "TT":
        print(i, Seq1[i:i+2])

#####################
print("--------")
#####################
print("-------")
#34

l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
print(max(l))
print(min(l))
l.sort()
print(l)

print(l[-1])
print(l[0])




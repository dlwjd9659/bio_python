#2
import math
r = 3
pi = math.pi

print(pi * r**2)


################
print("-----")
 
#3
n1 = 3
n2 = 5

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 % n2)
print(n1 ** n2)

################
print("-----")

#4
n1 = 3

if n1 % 2 == 0:
    print ("even")
else :
    print("odd")
    
################
print("-----")

#5
n1 = 21

if n1 % 3 == 0 and n1 % 7 == 0:
    print("multi of 3 and 7")
elif n1 % 3 == 0:
    print("multi of 3")
elif n1 % 7 == 0:
    print("multi of 7")
else:
    print("nothing")

################
print("-----")

#6

total = 0

for i in range(1, 11):
    total += i

print(total) #55

#################
print("-----")

#7

#for i in range(2, 9, 2):
#    for k in range(1, 10):
#        print(i, "*", k, "=", i*k)

#print()

#for i in range(2, 10):
#    for k in range(1, 10, 1):
#        if i % 2 == 0:
#            print(f"{i} x {k} = {i*k}")


##################
print("-----")

#8
n = 5
total = 1

while n > 0:
    total *= n
    n -= 1
    

print(total)

#################
print("-----")

#9
def greet() -> None: #return값이 없다고 명시적인 표현
    print("Hello, Bioinformatics")
    
greet()
greet()

#################
print("-----")

#10
def mySum(n1: int, n2: int) -> None:
    print(f"{n1} + {n2} = {n1 + n2}")

mySum(2, 3)
mySum(5, 7)
mySum(10, 15)

    
#################
print("-----")

#13
#a = input("input :")
#print(a)
#print(f"Hello {a}")

#print(type(a)) #class

#################
print("-----")

#14
#a = input("input : ")
#if a.isdigit():
#    print('integer')
#elif a.isalpha():
#    print('string')
#else:
#    print('nothing')


        

#################
print("-----")

#21
In [6]: s = "AGTTTATAG"

In [7]: s[5]

In [8]: s[3:6]

In [9] : len(s)

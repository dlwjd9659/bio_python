import sys

def fibo(n : int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(sys.argv[1])

print(fibo(n))


#    for i in range(a-2):
#        new = l_fibo[i] + l_fibo[i+1]
#        l_fibo.append(new)
#    return l_fibo

#print(fibo(5))


e = 'variable e'
print(e)

from math import *
print(e)
print(pi)


########################

l_list = ['a', 'a', 'b', 'c']

#import collections #collection 안에 모든 클래스 모두 불러옴

from collections import Counter #counter의 클래스만 불러

#cnt = collections.Counter(l_list)
cnt = Counter(l_list)

print(cnt)

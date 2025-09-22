
from itertools import *
from fractions import *
import sys
s, zero, one, two, l = input (), '.', '-.', '--', -1
for i in range (len (s)):
    if i <= l:
        continue
    if s[i:i + 2] == two:
        l = i + 1
        print (2, end='')
    elif s[i:i + 2] == one:
        l = i + 1
        print (1, end='')
    else:
        l = i
        print (0, end='')
        


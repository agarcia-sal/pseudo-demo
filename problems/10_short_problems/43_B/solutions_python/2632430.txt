import re
s = ''.join(sorted(input()))
t = '.*'.join(sorted(''.join(input().split())))
print('YES' if re.search(t, s) else 'NO')
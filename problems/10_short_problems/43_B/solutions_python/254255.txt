s = input()
d = dict((c,s.count(c)) for c in s)
for c in input(): d[c] = d.get(c,0)-1
print('NO' if [p for p in list(d.items()) if p[0]!=' ' and p[1]<0] else 'YES')

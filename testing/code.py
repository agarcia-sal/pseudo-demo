a = input()

a = a.replace('dot', '.')
a = a.replace('at', '@')

if a and a[0] == '.':
    a = 'dot' + a[1:]
if a and a[0] == '@':
    a = 'at' + a[1:]

co = 0
c = []

for i in a:
    if i == '@':
        if co > 0:
            c.append('at')
            co = 1
        else:
            c.append('@')
            co = 1
    else:
        c.append(i)

c = ''.join(c)

if c and c[-1] == '.':
    c = c[:-1] + 'dot'

print(c)
n = int(input())
b = [True] * n
j = 0
i = 1

while i <= 500000:
    if b[j]:
        b[j] = False  # Mark current index as False
    i += 1
    j = (j + i) % n  # Update index for the next iteration

x = [value for value in b if value]

if len(x) == 0:
    print('YES')  # All elements were marked False
else:
    print('NO')   # There are still True elements in the list

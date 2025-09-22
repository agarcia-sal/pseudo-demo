M = eval(input()) + 1
n = [0] * M
for i in range(2, M):
    if not n[i]:
        for j in range(2 * i, M, i):
            n[j] += 1
print(len([x for x in n if x == 2]))
            
